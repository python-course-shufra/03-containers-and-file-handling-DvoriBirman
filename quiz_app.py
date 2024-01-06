import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv
    subject=sys.argv[1]
    num=int(sys.argv[2])

    # 2. Open the correct file open(rf'questions\<filename>.txt)'
    file=open(rf'questions\{subject}.txt')
    print(file)

    # 3. Iterate over the file
    countQues=1
    countCorrect=0
    parts=[]
    question=''
    correct=''
    answers=[]
    for l in file:
      if(countQues>num):
       break
      parts=l.split(';')
      question=parts[0]
      correct=parts[1]
      answers=parts[2].rstrip().split(',')
      answers.append(correct)
      random.shuffle(answers)
      countQues+=1
      print(question)
    
      countLine=1
      for a in answers:
         print(f'{countLine}. {a}')
         countLine+=1
      countLine=1 
      if answers[int(input())-1]==correct:
         countCorrect+=1
    print(f'correct answers: {countCorrect}/{num}')  
     


     
    #       3.1. Parse the line (use s.split())
    #       3.2 Create a list of options
    #       3.3 random.shuffle(l)
    


if __name__ == '__main__':
    main()
