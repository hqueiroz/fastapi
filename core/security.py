from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha:str) -> bool:
    """
    FUNÇÃO PARA VERIFICAR SE A SENHA ESTÁ CORRETA, 
    COMPARANDO A SENHA EM TEXTO PURO, INFORMADA PELO USUÁRIO E HASH DA SENHA 
    QUE ESTARÁ SALVO NO BANCO DE DADOS DURANTE A CRIAÇÃO DA CONTA.
    """

    return CRIPTO.verify(senha, hash_senha)

def gerar_hash_senha(senha:str) -> str:
    """
    FUNÇÃO QUE GERA E RETORNA O HASH DA SENHA.
    """

    return CRIPTO.hash(senha)