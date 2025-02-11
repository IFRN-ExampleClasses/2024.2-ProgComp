'''
   EXEMPLO 08:

   Elabore um programa em Python que permita o cadastro de alunos e suas respectivas 
   disciplinas cursadas, bem como as notas obtidas em cada uma delas. 
   O programa deve funcionar da seguinte forma:

   - O usuário deverá informar a matrícula de um aluno e as disciplinas que ele já cursou;
   
   - Para cada disciplina, o programa solicitará duas notas;
   
   - O programa continuará pedindo disciplinas para o aluno até que o nome da disciplina 
     seja "FIM". Quando isso ocorrer, o processo de cadastro desse aluno será finalizado;
   
   - Caso a matrícula informada já tenha sido cadastrada anteriormente, o programa deverá 
     exibir a mensagem "MATRÍCULA JÁ CADASTRADA" e não permitirá o cadastro de novas disciplinas 
     para essa matrícula;
   
   - Caso uma disciplina já tenha sido cadastrada para a matrícula de um aluno, o programa deverá 
     exibir uma mensagem avisando que a disciplina já foi registrada e pedirá para o usuário 
     informar outra;
   
   - Utilize como padrão de notas valores inteiros entre 0 e 100;

   - O programa deverá continuar solicitando novas matrículas de alunos até que o usuário 
     opte por parar;
   
   - Ao final, o programa deverá exibir o dicionário com as matrículas dos alunos, as disciplinas que 
     cursaram e as respectivas notas.
'''

dictAlunos = dict()

