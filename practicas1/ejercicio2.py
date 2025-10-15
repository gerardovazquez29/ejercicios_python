
def requiere_auten(func):
    def recibe(usuario):
        if usuario.lower() == 'administrador':
            return func(usuario)
        else:
            return 'Acceso denegado'
    return recibe
@requiere_auten    
def admin_experto(usuario):
        return f'Bienvenido al panel, {usuario}'
    

print(admin_experto('administrador'))
print(admin_experto('Invitdo'))
