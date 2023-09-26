import os
import sys
import argparse
import paramiko
import tarfile
import gzip
import datetime

def create_backup(remote_host, remote_dir, local_dir, username, is_incremental, is_debug):
    # Создаем SSH-соединение с удаленным сервером
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(remote_host, username=username)
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации. Пожалуйста, проверьте имя пользователя и пароль.")
        return
    except paramiko.SSHException as e:
        print(f"Ошибка SSH: {e}")
        return
    except Exception as e:
        print(f"Ошибка при соединении с сервером: {e}")
        return

    # Определение текущей даты и времени для создания уникального имени бэкапа
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f"backup_{timestamp}.tar.gz"

    # Создание списка файлов/директорий для бэкапа
    remote_path = remote_dir.rstrip('/')
    local_path = os.path.join(local_dir, backup_name)

    tar_mode = 'w:gz' if not is_incremental else 'a:gz'
    with tarfile.open(local_path, tar_mode) as tar:
        if not is_incremental:
            # Создаем полный бэкап
            tar.add(remote_path, arcname=os.path.basename(remote_path))
        else:
            # Создаем инкрементальный бэкап
            tar.add(remote_path, arcname=os.path.basename(remote_path), recursive=False)

    # Закрытие SSH-соединения
    ssh.close()

    if is_debug:
        print(f"Создан бэкап: {local_path}")

def main():
    parser = argparse.ArgumentParser(description='Скрипт для создания бэкапов удаленного сервера.')
    parser.add_argument('-u', '--username', required=True, help='Имя пользователя для SSH-соединения')
    parser.add_argument('-s', '--server', required=True, help='IP-адрес удаленного сервера')
    parser.add_argument('-d', '--remote-dir', required=True, help='Удаленная директория для бэкапа')
    parser.add_argument('-l', '--local-dir', required=True, help='Локальная директория для хранения бэкапов')
    parser.add_argument('-i', '--incremental', action='store_true', help='Создать инкрементальный бэкап')
    parser.add_argument('--debug', action='store_true', help='Режим отладки')

    args = parser.parse_args()

    create_backup(args.server, args.remote_dir, args.local_dir, args.username, args.incremental, args.debug)

if __name__ == '__main__':
    main()
##############################################



Для создания скрипта бекапа с указанными функциональными требованиями, вы можете использовать Python и библиотеки, такие как paramiko для SSH-соединения с удаленным сервером, tarfile для создания архивов, gzip для сжатия данных и argparse для обработки аргументов командной строки. Вот пример такого скрипта:

python
Copy code
import os
import sys
import argparse
import paramiko
import tarfile
import gzip
import datetime

def create_backup(remote_host, remote_dir, local_dir, username, is_incremental, is_debug):
    # Создаем SSH-соединение с удаленным сервером
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(remote_host, username=username)
    except paramiko.AuthenticationException:
        print("Ошибка аутентификации. Пожалуйста, проверьте имя пользователя и пароль.")
        return
    except paramiko.SSHException as e:
        print(f"Ошибка SSH: {e}")
        return
    except Exception as e:
        print(f"Ошибка при соединении с сервером: {e}")
        return

    # Определение текущей даты и времени для создания уникального имени бэкапа
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f"backup_{timestamp}.tar.gz"

    # Создание списка файлов/директорий для бэкапа
    remote_path = remote_dir.rstrip('/')
    local_path = os.path.join(local_dir, backup_name)

    tar_mode = 'w:gz' if not is_incremental else 'a:gz'
    with tarfile.open(local_path, tar_mode) as tar:
        if not is_incremental:
            # Создаем полный бэкап
            tar.add(remote_path, arcname=os.path.basename(remote_path))
        else:
            # Создаем инкрементальный бэкап
            tar.add(remote_path, arcname=os.path.basename(remote_path), recursive=False)

    # Закрытие SSH-соединения
    ssh.close()

    if is_debug:
        print(f"Создан бэкап: {local_path}")

def main():
    parser = argparse.ArgumentParser(description='Скрипт для создания бэкапов удаленного сервера.')
    parser.add_argument('-u', '--username', required=True, help='Имя пользователя для SSH-соединения')
    parser.add_argument('-s', '--server', required=True, help='IP-адрес удаленного сервера')
    parser.add_argument('-d', '--remote-dir', required=True, help='Удаленная директория для бэкапа')
    parser.add_argument('-l', '--local-dir', required=True, help='Локальная директория для хранения бэкапов')
    parser.add_argument('-i', '--incremental', action='store_true', help='Создать инкрементальный бэкап')
    parser.add_argument('--debug', action='store_true', help='Режим отладки')

    args = parser.parse_args()

    create_backup(args.server, args.remote_dir, args.local_dir, args.username, args.incremental, args.debug)

if __name__ == '__main__':
    main()



Скрипт принимает следующие параметры:

-u или --username: Имя пользователя для SSH-соединения.
-s или --server: IP-адрес удаленного сервера.
-d или --remote-dir: Удаленная директория для бэкапа.
-l или --local-dir: Локальная директория для хранения бэкапов.
-i или --incremental: Опциональный флаг для создания инкрементального бэкапа.
--debug: Опциональный флаг для режима отладки.


  
#############################################
