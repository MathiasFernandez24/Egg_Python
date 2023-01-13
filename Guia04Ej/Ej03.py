usuarios = {'Brahms', 'Schubert', 'Vivaldi', 'Verdi', 'Tchaikovsky'}
admins = set()
admins.update({'Brahms', 'Verdi'})
admins.discard('Brahms')
admins.add('Tchaikovsky')


print(usuarios)
print(admins)
