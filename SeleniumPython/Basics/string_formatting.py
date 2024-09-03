x = 'Python'
y = 'Class'
z = 'abc'
q = 'academy'

print('Welcome to %s %s from %s %s' %(x, y, z, q))
print('Welcome to {} {} from {} {}'.format(x, y, z, q))
print('Welcome to {3} {2} from {1} {0}'.format(x, y, z, q))
print('Welcome to {language} {class_name} from {org_name} {academy}'.format(language = x,
                                                                            class_name = y,
                                                                            org_name = z,
                                                                            academy = q))
