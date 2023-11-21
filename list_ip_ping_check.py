import subprocess

# Чтение списка IP адресов из файла
with open('list_ip.txt', 'r') as file:
    ip_addresses = file.readlines()

# Пингуем каждый IP адрес
with open('list_ip_check.txt', 'w') as output_file:
    for ip in ip_addresses:
        ip = ip.strip()  # Удаляем лишние пробелы и символы переноса строки
        result = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            output_file.write(f"{ip} available\n")
        else:
            output_file.write(f"{ip} unavailable 100% packet loss\n")