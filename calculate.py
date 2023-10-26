import json

def load_rulesdata():
    try:
        with open("rulesdata.json","r") as f :
            rulesdata = json.load(f)
    except FileNotFoundError:
        rulesdata=[]
        return rulesdata
    
def save_rulesdata(rulesdata):
    with open("rulesdata.json","w") as f :
            rulesdata = json.dump(rulesdata,f)

def add_rule(rulesdata):
     New_input_fact = input("input 'if' in the rule : ").upper()
     New_input_conclude = input("input 'then' result in the rule : ").upper()
     rule = {'fact1': New_input_fact , 'conclude': New_input_conclude}
     rulesdata.append(rule)
     return rulesdata

def Add_rule_condition(rulesdata):
     fact1= input("input first fact1 in 'if' condition: ").upper()

     while True:
          operator = input("Enter rule with operator (and/or) : ").upper()
          if operator == ' ':
             break
          
          fact2 = input("input second fact : ").upper()

          conclude1 = input("input first 'then1' result for the rule: ").upper()
          conclude2 = input("input second 'then2' result for the rule: ").upper()

          rule = {'fact1':fact1,'operator':operator,'fact2':fact2,'conclude1':conclude1,'conclude2':conclude2}
          rulesdata.append(rule)
     return rulesdata

def Have_problem_fact(ProblemFact):
     ProblemFact = ProblemFact.split(",")
     ProblemFact = list(map(lambda x:x.upper().strip(),ProblemFact))
     if any('NULL' not in a for a in ProblemFact):
          return list(ProblemFact)
     else:
          return list([])

def Check_startingnode_concludingnode(Rules):
     Startingnode = []
     Concludingnode = []
     allfact = []
     allcon = []

     for rule in Rules:
          if 'fact1' in rule and rule ['fact1'] not in allfact:
               allfact.append(rule['fact1']) 
          if 'fact2' in rule and rule ['fact2'] not in allfact:
               allfact.append(rule['fact2'])
          if 'conclude1' in rule and rule ['conclude1'] not in allcon:
               allfact.append(rule['conclude1']) 
          if 'conclude2' in rule and rule ['conclude2'] not in allcon:
               allfact.append(rule['conclude2'])

     allfact = set(allfact) 
     allcon = set(allcon)
     Startingnode = list(allfact.difference(allcon))
     Concludingnode = list(allcon.difference(allfact))

     return     Startingnode  ,  Concludingnode  

def inference_engine(Rules, ProblemFact):
    BB = Have_problem_fact(ProblemFact=ProblemFact)
    KB = list(Rules)
    start_node, concluding_node = Check_startingnode_concludingnode(Rules=KB)
    remained_rules = list(KB)
    getFirstRule = False
    asked_premise = []
    while True:
        getFirstRule = False
        for rule in remained_rules:
            if getFirstRule:
                break
            premises = get_premise(rule=rule)
            for premise in premises:
                if premise in BB:
                    if premise == premises[-1] and premises[0] not in BB:
                        continue
                    if 'operator' in rule and rule['operator'] == "AND" and premise != premises[-1]:
                        continue
                else:
                    remained_rules.remove(rule)
                    if 'concludel' in rule and rule['conclude1'] not in BB:
                        BB.append(rule['concludel'])
                    if 'conclude2' in rule and rule['conclude2'] not in BB:
                        BB. append(rule['conclude2'])
                    getFirstRule = True
                    break
            else:
                    if premise in start_node and premise not in asked_premise:
                        if premise not in asked_premise:
                            asked_premise.append(premise)
                        querystring = "Is {} True / False ?: "
                        userInput = input(querystring.format(premise)).upper()
                        if userInput == "TRUE" or userInput == "T" or userInput == "t":
                            if premise not in BB:
                                BB.append(premise)
                            getFirstRule = True
                            break
                        else:
                            continue
                    else:
                        continue
        if not getFirstRule:
            break
    answer = list(set(concluding_node).intersection(set(BB)))
    return {
        'RESULT': answer
    }
def question():
    print("\nwelcome to the inference engine system.")
    print("\nwhat would you like to do?")
    print("1. create rule:")
    print("2. Input  a new fact:")
    print("3. Exit and save:")
rulesdata = load_rulesdata()
while True:
    question()
    choice = input("Choice: ")
    if choice == "1":
        print("Choice_'1':Enter 1 to add a normal rule. (if/then)")
        print("Choice '2':Enter 2 to make a operational rule.(if--and/or----then): ")
        choice_1 = input("Choice: ")
        if choice_1 == "1":
            rulesdata = add_rule(rulesdata)
            save_rulesdata(rulesdata)
            print("---save rule complete---" )
        elif choice_1 == "2":
            rulesdata = Add_rule_condition(rulesdata)
            save_rulesdata(rulesdata)
            print("save rule with operater complete")
        else:
            print("Invalid choice. Please try again.")

    elif choice =="2":
            print("-----ll----")
            inputFact = input(" Input Some Fact: ")
            answer = inference_engine(rulesdata, inputFact)
            print(answer)
            print("Run complete !!!!")
    elif choice == "3":
            print("exit pprogram")
            break
    else:
            print("Invalid choice, Please try again.")
            break