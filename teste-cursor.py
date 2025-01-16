import paramiko
import time

def ssh_connect(hostname, username, password, port=22):
    try:
        # Criar uma instância do cliente SSH
        ssh_client = paramiko.SSHClient()
        
        # Adicionar política para chaves desconhecidas
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Realizar a conexão
        print(f"Conectando ao servidor {hostname}...")
        ssh_client.connect(
            hostname=hostname,
            username=username,
            password=password,
            port=port
        )
        print("Conexão estabelecida com sucesso!")
        
        return ssh_client
    
    except paramiko.AuthenticationException:
        print("Erro: Falha na autenticação. Verifique usuário e senha.")
        return None
    except paramiko.SSHException as ssh_exception:
        print(f"Erro SSH: {ssh_exception}")
        return None
    except Exception as e:
        print(f"Erro: {str(e)}")
        return None

def execute_command(ssh_client, command):
    try:
        if ssh_client:
            # Executar comando
            stdin, stdout, stderr = ssh_client.exec_command(command)
            
            # Aguardar a execução do comando
            time.sleep(1)
            
            # Ler a saída
            output = stdout.read().decode()
            error = stderr.read().decode()
            
            if error:
                print(f"Erro ao executar comando: {error}")
            else:
                print(f"Saída do comando:\n{output}")
                
    except Exception as e:
        print(f"Erro ao executar comando: {str(e)}")

def main():
    # Configurações de conexão
    hostname = "192.168.15.43"  # Substitua pelo endereço do seu servidor
    username = "rafael"       # Substitua pelo seu usuário
    password = "m4f5d90S!@"         # Substitua pela sua senha
    
    # Conectar ao servidor
    ssh_client = ssh_connect(hostname, username, password)
    
    if ssh_client:
        try:
            # Exemplo de comandos para executar
            commands = [
                "ls -la",
                "pwd",
                "whoami"
            ]
            
            # Executar cada comando
            for command in commands:
                print(f"\nExecutando comando: {command}")
                execute_command(ssh_client, command)
                
        finally:
            # Fechar a conexão
            ssh_client.close()
            print("\nConexão SSH encerrada.")

if __name__ == "__main__":
    main()
