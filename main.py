from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Machine, MemUsage, RefTime, CpuUsage, DiskUsage, UsersConnected, ProccessRunning, ConnectionActive
from ssh import SSH
from paramiko import SSHException
from datetime import datetime
import yaml


if __name__ == '__main__':

    try:
        with open('config_db.yaml') as yaf:
            database_conf = yaml.full_load(yaf)
    except IOError:
        print("Error: File config_db.yaml not found.") 


    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(database_conf['database']['username'],
                                                                   database_conf['database']['password'],
                                                                   database_conf['database']['hostname'],
                                                                   database_conf['database']['port'],
                                                                   database_conf['database']['database_name']))

    Session = sessionmaker(bind=engine)
    session = Session()

    qry_all_machines = session.query(Machine)

    for machine in qry_all_machines:

        data_e_hora_atuais = datetime.now()

        ref_time = RefTime(time_ref=data_e_hora_atuais, machine_id=machine.id)
        session.add(ref_time)
        session.commit()


        try:
            con_ssh = SSH(hostname=machine.hostname, username=machine.username)


            ca = ConnectionActive(connected='YES',ref_time_id=ref_time.id)
            session.add(ca)
            session.commit()



            disk_usage = con_ssh.cmd_disk_usage()
            for disk in disk_usage:
                du = DiskUsage(filesystem=disk['filesystem'],
                            type=disk['type'],
                            size=disk['size'],
                            used=disk['used'],
                            mounted_on=disk['mounted_on'],
                            available=disk['available'],
                            use_percent=disk['use_percent'],
                            ref_time_id=ref_time.id)
                session.add(du)
                session.commit()
            

            cpu_usage = con_ssh.cmd_cpu_usage()
            for cpu in cpu_usage:
                cpuu = CpuUsage(cpu=cpu['cpu'],           
                                value_percent=cpu['value_percent'],
                                ref_time_id=ref_time.id)

                session.add(cpuu)
                session.commit()

            users_connected = con_ssh.cmd_users_connected()
            for user in users_connected:
                uc = UsersConnected(user=user['user'],
                                    tty=user['tty'],
                                    time=user['time'],
                                    from_s=user['from'],
                                    ref_time_id=ref_time.id)
                session.add(uc)
                session.commit()
            
            proccess_running = con_ssh.cmd_proccess_running()
            for pr in proccess_running:
                prr = ProccessRunning(user=pr['user'],
                                    pid=pr['pid'],
                                    vsz=pr['vsz'],
                                    rss=pr['rss'],
                                    tty=pr['tty'],
                                    stat=pr['stat'],
                                    start=pr['start'],
                                    time=pr['time'],
                                    command=pr['command'],
                                    cpu_percent=['cpu_percent'],
                                    men_percent=['men_percent'],
                                    ref_time_id=ref_time.id)
                session.add(prr)
                session.commit()


            mem_usage = con_ssh.mem_usage()
            mup = MemUsage(mem_usage_percent=float(mem_usage['mem_usage_percent']),ref_time_id=ref_time.id)
            session.add(mup)
            session.commit()            
        except SSHException:
            ca = ConnectionActive(connected='NO',ref_time_id=ref_time.id)
            session.add(ca)
            session.commit()



        
        


    

     







