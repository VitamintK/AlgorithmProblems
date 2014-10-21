import sys
from collections import defaultdict

sys.setrecursionlimit(10000)
def make_dict(bigstring):
    alphadict = defaultdict(list)
    for (index, ch) in enumerate(bigstring):
        alphadict[ch].append(index)
    return alphadict

def get_best_pal(alphadict, bigstring):
    return rec_best_pal(0, len(bigstring), alphadict, bigstring)

def rec_best_pal(index, end, alphadict, bigstring):
    try:
        if index >= end:
            raise Exception
        ch = bigstring[index]
    except:
        return 1
    best_match = -1
    for match in reversed(alphadict[ch]):
        #print('line 17 {}'.format(ch))
        if match < end:
            best_match = match
            break
    if index < best_match:
        if index == best_match -1:
            return 2
        else:
            return max(2 + rec_best_pal(index+1, best_match, alphadict, bigstring),
                       rec_best_pal(index+1, end, alphadict, bigstring))
    else:
        return rec_best_pal(index+1, end, alphadict, bigstring)

def main():
    bigstring = 'rmubflelopzfhomshwaqsxodeoivksuirntceqtbhfrbjqtxttsoemkqginnwnuabxwxahprutzzmtqathdbaniysxjzjjyydmmmljnlqtlaeuaksxvaggolyovkjovzjswuuiysbxyuwvmvbugcazgvbiniqnlsojecpktsnueacfkfizqdeetagjulqtxsbybwiszatoicfxfutkiqwctqhdoxuqrmkxawcwiyotytacwqjjqwmpfficveqybnbgblrvdeucjhnxhiefqkmnapyffvrbuwqtipaepvhekwznewpybvoadwkyzxrmddqfzjofznaxknylledtyvaixpeezpjkhwneqzkivmcqjxjxzzyusgdsqkgzvxybqsfaizhuvglqgxcotfzxkckajjzcpabddgxnxgvsfjnaeykjwkxqqguawgpfhpmvvatqqhfzfhjvlrlcmxgbnduzotcktokxiaoeqookxkzrtomsfifexcquwumczgbnwugigviusrreunmfauqoyjkbhylzuqfmzebccsijzwsgnlqtzormydjvxsemnlvsuvtvhysawexotieivlqsrokmaiifjkwhldhkporegkockrxgjrgcxgmuqdvzetihxnyeizpfqkfupztkxcwxxdbaenwokgngpalaqehxcwimvygfdrgqqpjizltateqdysjpygxhjvzvxohnmigmtaqprjgnktanhpsucbgkqpisovskfhesxsnwytdwzzxrketswycywelsesrqpqkfcxbwmwqejhxktzsvlphgnjccdcotiwtocyxjimchuatadlatrcidsayjzihsktrhibsymtjkrwzopzazqqiipsxxzxgbcwqdvxtqpjuqrwztyenbxoyurliwgpxcvvnbioxgqwpsnyqbnupvpmevbbrfiufoxlpibqmsmybtwmxaadpvwbqzedwxmjsoikpxxqnxqiqmekxdmxdxxbyetvnrsylkutqvlryjvbiuqcxuoafboadwaboilsgdammioynnaicvbzybvmrkatxazebujwevcbfojdqynggwqtocrciynbsutonccpdvyybalmddtpprpfwxwjzevcyymzaibtflgijrjtyvfyyeizqbdtscndsefailfrggxskwykjbjgowxagiyutkviumzsuzdmeyukonirampwfyujpyjiceevzlepqeglyprfsxsgnyjqpcosfogykfsfntgrqipeclwttwezpititqjapumokntkypwofzbrugvqaptupzjovbacqkrvpsdncmnmeysdbkltqrbnbqlxumdpwdwktabldlpvfvgjngoczgabmbljxqldyhzaxgbxocpmgpeceuabwciratjijpkzxqyfbuemdbujcuawujhbgmyvylksrxxkcbvzgxksceiivsuvxnemvlsjnabbsxlwtgjdwkzzvwnyeclohimhelafrratvuryfqjcuoooetyxnwtdeydxqnnwzaikwstuhuycxffinhofscipnxxvjfpwzmoybocmkhmusolxdzgevfohcfuffujdkyxtspigsurbiexmiuxeolbywkwvnwxblsrypiycbbizwxzoehetdtbnbmnrjbzsngvrsvakgbqhasqqvtmdrzulshxcuzegncpdjrxjyfvwqdcvjcpsjefrrqifzohzdrrmrqgaaaefaoveymxisizzkvhocshagdtzlfxklcevvlsvlqcoqphntranmwyckbatsggkzwawyyvvxsclftjqasktzmdxcwovaskrgbqlupxgduxzfbsqhlrwhrzunowdrcuavnwbircugdvjpxcclmdwjvptmekspqltjrikqkcyiqvpuidpitnmankfkrwojmqznblfzhbjcdrgaurzxaynfdgkcsxcqhtffbtshgesdvazizqfpmhxjynsuakojvoyyyhfuyzxbuigniztulzb'
    #bigstring = open('ieeepalindrome.txt', 'r').read().strip()
    #bigstring = sys.stdin.read().strip()
    alphadict = make_dict(bigstring)
    best_pal = get_best_pal(alphadict, bigstring)
    print(best_pal)
    
main()
