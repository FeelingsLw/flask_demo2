from random import randint

person = ['赵文欢', '李笑', '李樾', '杨乐贵', '许一博']
print('第一组：辛冀航,', end='')
for i in range(3):
    print(person.pop(randint(0, 4 - i)), end='，')
print()
print('第二组：廖千里,', end='')
for p in person:
    print(p, end='，')

'''
第一组：辛冀航,李樾，许一博，李笑， 
第二组：廖千里,赵文欢，杨乐贵，
项目架构：模型设计
'''
