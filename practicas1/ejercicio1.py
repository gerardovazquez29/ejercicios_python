# funciones de orden superior
def requiere_auten(func):
    def recibe(usuario):
        if usuario.lower() == 'administrador':
            return func(usuario)
        else:
            return 'Acceso denegado'
    return recibe
    
def admin_experto(usuario):
        return f'Bienvenido al panel, {usuario}'
    
autenticador = requiere_auten(admin_experto)
print(autenticador('administrador'))
print(autenticador('Invitdo'))

# Decoradores
