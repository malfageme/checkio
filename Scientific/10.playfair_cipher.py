import string
from itertools import product

class Playfair_cipher(object):   
    
    def __init__(self,key):
        self.key = key
        self.table = self.build_table(key)
    
    def build_table(self,key):
        table = ''
        for c in key+string.ascii_lowercase+string.digits:
            if c not in table: table+=c
        return table
    
    def get_coor(self,char):
        index = self.table.index(char)
        return (index/6,index%6)

    def get_char(self,coor):
        return self.table[(coor[0]%6)*6+(coor[1]%6)]

    def get_table(self):
        return self.table
    
    def prepare_text(self,text):
        new_text = ''
        valid_chars = string.ascii_lowercase+string.digits
        i, new_i = 0, 0
        prep_text=text.lower()
        while i<len(prep_text):
            if prep_text[i] not in valid_chars:
                i+=1
                continue
            if new_i%2==0:
                new_text+=prep_text[i]
                new_i+=1
                i+=1
            else:
                if new_text[-1]==prep_text[i]:
                    new_c = 'z' if new_text[-1]=='x' else 'x'
                else:
                    new_c=prep_text[i]
                    i+=1
                new_text+=new_c
                new_i+=1
        if len(new_text)%2==1:
            new_text+='x' if new_text[-1] == 'z' else 'z'
        return [new_text[i*2:i*2+2] for i in range(len(new_text)/2)]
    
    def encode(self,text):
        prepared_text=self.prepare_text(text)
        ct=''
        for d in prepared_text:
            coor_pt_1=self.get_coor(d[0])
            coor_pt_2=self.get_coor(d[1])
            # Check same row
            if coor_pt_1[0]==coor_pt_2[0]:
                coor_ct_1=(coor_pt_1[0],coor_pt_1[1]+1)
                coor_ct_2=(coor_pt_2[0],coor_pt_2[1]+1)
            # Check same column
            elif coor_pt_1[1]==coor_pt_2[1]:
                coor_ct_1=(coor_pt_1[0]+1,coor_pt_1[1])
                coor_ct_2=(coor_pt_2[0]+1,coor_pt_2[1])
            # Check square
            else:
                coor_ct_1=(coor_pt_1[0],coor_pt_2[1])
                coor_ct_2=(coor_pt_2[0],coor_pt_1[1])
            ct+=self.get_char(coor_ct_1)+self.get_char(coor_ct_2)
        return ct

    def decode(self,ct):        
        pt=''
        for d in [ct[i*2:i*2+2] for i in range(len(ct)/2)]:
            coor_pt_1=self.get_coor(d[0])
            coor_pt_2=self.get_coor(d[1])
            # Check same row
            if coor_pt_1[0]==coor_pt_2[0]:
                coor_ct_1=(coor_pt_1[0],coor_pt_1[1]-1)
                coor_ct_2=(coor_pt_2[0],coor_pt_2[1]-1)
            # Check same column
            elif coor_pt_1[1]==coor_pt_2[1]:
                coor_ct_1=(coor_pt_1[0]-1,coor_pt_1[1])
                coor_ct_2=(coor_pt_2[0]-1,coor_pt_2[1])
            # Check square
            else:
                coor_ct_1=(coor_pt_1[0],coor_pt_2[1])
                coor_ct_2=(coor_pt_2[0],coor_pt_1[1])
            pt+=self.get_char(coor_ct_1)+self.get_char(coor_ct_2)
        return pt
        
    def print_table(self):
        print " KEY TABLE "
        table_list=[self.table[r*6:r*6+6] for r in range(6)]
        for r in table_list: print " ".join(r)
            


def encode(message, key):
    cipher=Playfair_cipher(key)
    return cipher.encode(message)


def decode(secret_message, key):
    cipher=Playfair_cipher(key)
    return cipher.decode(secret_message)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"

