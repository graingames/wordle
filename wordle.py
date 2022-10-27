import random, os
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ran = False

class letter():
    def __init__(self, name): 
        self.id = name
        self.positions = []
        self.frequency = 0
        self.rem_array = []
    def add_pos(self, pos):
        self.positions.append(pos)
        self.frequency += 1
    def check(self, position):
        if position in self.positions: return True

def check(word_submit, let_array, letters_in_word):
    word_submit += "------"
    word_submit = word_submit[:6]
    return_array = [0 for _ in range(6)]
    yellows = [0 for _ in let_array]
    for i, l in enumerate(word_submit):
        if l in letters_in_word:
            for j, let in enumerate(let_array):
                if let.id == l:
                    if let.check(i): 
                        return_array[i] = 2
                        yellows[j] += 1
                    else: 
                        let.rem_array.append(i)
                        return_array[i] = let.id
    for i, let in enumerate(let_array):
        for _ in let.rem_array:
            if yellows[i] < let.frequency:
                for j, ele in enumerate(return_array):
                    if ele == let.id:
                        return_array[j] = 1
                        yellows[i] += 1
    return(return_array)

def init_letters(word):
    letter_array = [letter(alphabet[i]) for i in range(26)]
    for i, l in enumerate(word):
        for let in letter_array:
            if let.id == l: let.add_pos(i)
    letter_array_copy = letter_array.copy()
    offset = 0
    for j, let in enumerate(letter_array_copy):
        if let.frequency == 0: 
            letter_array.pop(j - offset)
            offset+=1
    letters_in_word = ""
    for let in letter_array: letters_in_word += let.id
    return letter_array, letters_in_word

def draw(word_submit, let_array, letters_in_word, attempt_no = 0):
    z = len(word_submit)
    word_submit += "-------"
    attempt_no +=1
    word_submit = word_submit[:6]
    wrong_attempts = []
    string = f"Attempt {attempt_no}) "
    check_result = check(word_submit, let_array, letters_in_word)
    for i, result in enumerate(check_result):
        if result == 2: string += word_submit[i].upper()
        elif result == 1: string += word_submit[i]
        elif word_submit[i].lower() in "qwertyuiopasdfghjklzxcvbnm":
            string += "*"
            wrong_attempts.append(word_submit[i])

    if wrong_attempts == [] and z >= 6: return string, -1
    return string, wrong_attempts
        
def draw_prev(words, let_array, letters_in_word):
    ret_str = ""
    i = 0
    for word in words:
        word += "~~~~~~"
        string, _ = draw(word[:6], let_array, letters_in_word, i+1)
        ret_str+=f"\n{string}"
        i+=1
    return ret_str

words = ["better", "beyond", "bishop", "border", "bottle", "bottom", "bought", "branch", "breath", "bridge", "bright", "broken", "budget", "burden", "bureau", "button", "camera", "cancer", "cannot", "carbon", "career", "castle", "casual", "caught", "center", "centre", "chance", "change", "charge", "choice", "choose", "chosen", "church", "circle", "client", "closed", "closer", "coffee", "column", "combat", "coming", "common", "comply", "copper", "corner", "costly", "county", "couple", "course", "covers", "create", "credit", "crisis", "custom", "damage", "danger", "dealer", "debate", "decade", "decide", "defeat", "defend", "define", "degree", "demand", "depend", "deputy", "desert", "design", "desire", "detail", "detect", "device", "differ", "dinner", "direct", "doctor", "dollar", "domain", "double", "driven", "driver", "during", "easliy", "eating", "editor", "effect", "effort", "eighth", "either", "eleven", "emerge", "empire", "employ", "enable", "ending", "energy", "engage", "engine", "enough", "ensure", "entire", "entity", "equity", "escape", "estate", "ethnic", "exceed", "except", "excess", "expand", "expect", "expert", "export", "extend", "extent", "fabric", "facing", "factor", "failed", "fairly", "fallen", "family", "famous", "father", "fellow", "female", "figure", "filing", "finger", "finish", "fiscal", "flight", "flying", "follow", "forced", "forest", "forget", "formal", "format", "former", "foster", "fought", "fourth", "french", "friend", "future", "garden", "gather", "gender", "german", "global", "golden", "ground", "growth", "guilty", "handed", "handle", "happen", "hardly", "headed", "health", "height", "hidden", "holder", "honest", "impact", "import", "income", "indeed", "injury", "inside", "intend", "intent", "invest", "island", "itself", "jersey", "joseph", "junior", "killed", "labour", "latest", "latter", "launch", "lawyer", "leader", "league", "leaves", "legacy", "length", "lesson", "letter", "likely", "linked", "liquid", "listen", "little", "living", "losing", "lucent", "luxury", "mainly", "making", "manage", "manner", "manual", "margin", "marine", "marked", "market", "martin", "master", "matter", "mature", "medium", "member", "memory", "mental", "merely", "merger", "method", "middle", "miller", "mining", "minute", "mirror", "mobile", "modern", "modest", "module", "moment", "morris", "mostly", "mother", "motion", "moving", "murder", "museum", "mutual", "myself", "narrow", "nation", "native", "nature", "nearby", "nearly", "nights", "nobody", "normal", "notice", "notion", "number", "object", "obtain", "office", "offset", "online", "option", "orange", "origin", "output", "oxford", "packed", "palace", "parent", "partly", "patent", "people", "period", "permit", "person", "phrase", "picked", "planet", "player", "please", "plenty", "pocket", "police", "policy", "prefer", "pretty", "prince", "prison", "profit", "proper", "proven", "public", "pursue", "raised", "random", "rarely", "rather", "rating", "reader", "really", "reason", "recall", "recent", "record", "reduce", "reform", "regard", "regime", "region", "relate", "relief", "remain", "remote", "remove", "repair", "repeat", "replay", "report", "rescue", "resort", "result", "retail", "retain", "return", "reveal", "review", "reward", "riding", "rising", "robust", "ruling", "safety", "salary", "sample", "saving", "saying", "scheme", "school", "screen", "search", "season", "second", "secret", "sector", "secure", "seeing", "select", "seller", "senior", "series", "server", "settle", "severe", "sexual", "should", "signal", "signed", "silent", "silver", "simple", "simply", "single", "sister", "slight", "smooth", "social", "solely", "sought", "source", "soviet", "speech", "spirit", "spoken", "spread", "spring", "square", "stable", "status", "steady", "stolen", "strain", "stream", "street", "stress", "strict", "strike", "string", "strong", "struck", "studio", "submit", "sudden", "suffer", "summer", "summit", "supply", "surely", "survey", "switch", "symbol", "system", "taking", "talent", "target", "taught", "tenant", "tender", "tennis", "thanks", "theory", "thirty", "though", "threat", "thrown", "ticket", "timely", "timing", "tissue", "toward", "travel", "treaty", "trying", "twelve", "twenty", "unable", "unique", "united", "unless", "unlike", "update", "useful", "valley", "varied", "vendor", "versus", "victim", "vision", "visual", "volume", "walker", "wealth", "weekly", "weight", "wholly", "window", "winner", "winter", "within", "wonder", "worker", "wright", "writer", "yellow"]
random.shuffle(words)
selected_word = words.pop()
letter_array, letters_in_word = init_letters(selected_word)
input("Here is how to play (I am expecting you to know how wordle works and you played it)\nInstead of the letters being grey/gray they will become *\nInstead of the letters going yellow they will be lowercase\nInstead of letters going green they will go UPPERCASE\nAll of the letters you got right will be listed below.")
os.system("cls")
attempts = []
wrong_attempts = []
for i in range(6):
    str2 = ""
    word_submit = input(f"Enter your attempt ({i+1}): ").lower()
    string, wrong = draw(word_submit, letter_array, letters_in_word)
    if wrong == -1: break
    for w in wrong: 
        if w not in wrong_attempts: wrong_attempts.append(w)
    os.system("cls")
    str1 = draw_prev(attempts, letter_array, letters_in_word)
    for a in wrong_attempts: str2+=a
    attempts.append(word_submit)
    print(f"{string}{str1}\n\nWrong attempts {str2}\n\n") 
else:
    input(f"You lost!\nThe word was {selected_word}.")
    ran = True

if not ran:
    input("Congratulations winning!")
