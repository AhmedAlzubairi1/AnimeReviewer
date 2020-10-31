import re
import copy
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
mark_as_deleted={

}
animeInfo=[
    {
    "id":1,
    "title": "Naruto",
    "image": "https://cdn.myanimelist.net/images/anime/13/17405.jpg",
    "info": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.Now, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.",
    "year": 2002,
    "reviews": [["I loved Naruto",False], ["Naruto was okay",False], ["wasn't the biggest fan",False], ["Yah are bugging, naruto is amazing",False]]
},
{
    "id":2,
    "title": "Hunter x Hunter",
    "image": "https://cdn.myanimelist.net/images/anime/11/33657.jpg",
    "info": "Hunter x Hunter is set in a world where Hunters exist to perform all manner of dangerous tasks like capturing criminals and bravely searching for lost treasures in uncharted territories. Twelve-year-old Gon Freecss is determined to become the best Hunter possible in hopes of finding his father, who was a Hunter himself and had long ago abandoned his young son. However, Gon soon realizes the path to achieving his goals is far more challenging than he could have ever imagined.Along the way to becoming an official Hunter, Gon befriends the lively doctor-in-training Leorio, vengeful Kurapika, and rebellious ex-assassin Killua. To attain their own goals and desires, together the four of them take the Hunter Exam, notorious for its low success rate and high probability of death. Throughout their journey, Gon and his friends embark on an adventure that puts them through many hardships and struggles. They will meet a plethora of monsters, creatures, and characters—all while learning what being a Hunter truly means."
    ,"year": 2011,
    "reviews": [["I loved Hunter X Hunter",False]]
},
{
    "id":3,
    "title":     "Fullmetal Alchemist: Brotherhood",
    "image": "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
    "info": "Alchemy is bound by this Law of Equivalent Exchange—something the young brothers Edward and Alphonse Elric only realize after attempting human transmutation: the one forbidden act of alchemy. They pay a terrible price for their transgression—Edward loses his left leg, Alphonse his physical body. It is only by the desperate sacrifice of Edward's right arm that he is able to affix Alphonse's soul to a suit of armor. Devastated and alone, it is the hope that they would both eventually return to their original bodies that gives Edward the inspiration to obtain metal limbs called automail and become a state alchemist, the Fullmetal Alchemist.Three years of searching later, the brothers seek the Philosopher's Stone, a mythical relic that allows an alchemist to overcome the Law of Equivalent Exchange. Even with military allies Colonel Roy Mustang, Lieutenant Riza Hawkeye, and Lieutenant Colonel Maes Hughes on their side, the brothers find themselves caught up in a nationwide conspiracy that leads them not only to the true nature of the elusive Philosopher's Stone, but their country's murky history as well. In between finding a serial killer and racing against time, Edward and Alphonse must ask themselves if what they are doing will make them human again... or take away their humanity."
    ,"year": 2009,
    "reviews": [["I loved Full metal Alchemist",False]]
},
{
    "id":4,
    "title":     "Bleach",
    "image": "https://cdn.myanimelist.net/images/anime/3/40451.jpg",
    "info":"Ichigo Kurosaki is an ordinary high schooler—until his family is attacked by a Hollow, a corrupt spirit that seeks to devour human souls. It is then that he meets a Soul Reaper named Rukia Kuchiki, who gets injured while protecting Ichigo's family from the assailant. To save his family, Ichigo accepts Rukia's offer of taking her powers and becomes a Soul Reaper as a result. However, as Rukia is unable to regain her powers, Ichigo is given the daunting task of hunting down the Hollows that plague their town. However, he is not alone in his fight, as he is later joined by his friends—classmates Orihime Inoue, Yasutora Sado, and Uryuu Ishida—who each have their own unique abilities. As Ichigo and his comrades get used to their new duties and support each other on and off the battlefield, the young Soul Reaper soon learns that the Hollows are not the only real threat to the human world.",
    "year": 2004,
    "reviews": []
},
{
    "id":5,
    "title":     "Suzumiya Haruhi no Shoushitsu",
    "image": "https://cdn.myanimelist.net/images/anime/2/73842.jpg",
    "info":"One cold Christmas day, Kyon heads over to school and the SOS Brigade's holiday celebration, only to realize that Haruhi Suzumiya seems to have disappeared. Moreover, no one even remembers her or the SOS Brigade; Mikuru Asahina knows nothing and is now afraid of him, and Itsuki Koizumi has also gone missing. The Literature Club, formed only by an uncharacteristically shy Yuki Nagato, now occupies the old SOS club room. Suzumiya Haruhi no Shoushitsu is based on the fourth light novel of the acclaimed Haruhi series and is set after the events of the anime series. Not uncultured in the supernatural, Kyon will have to deal with his whole life turned upside down like a bad joke, and maybe it's better that way."
    ,"year": 2010,
    "reviews": []
},
{
    "id":6,
    "title":     "Yakusoku no Neverland",
    "image": "https://cdn.myanimelist.net/images/anime/1125/96929.jpg",
    "info":"Surrounded by a forest and a gated entrance, the Grace Field House is inhabited by orphans happily living together as one big family, looked after by their Mama, Isabella. Although they are required to take tests daily, the children are free to spend their time as they see fit, usually playing outside, as long as they do not venture too far from the orphanage—a rule they are expected to follow no matter what. However, all good times must come to an end, as every few months, a child is adopted and sent to live with their new family... never to be heard from again. However, the three oldest siblings have their suspicions about what is actually happening at the orphanage, and they are about to discover the cruel fate that awaits the children living at Grace Field, including the twisted nature of their beloved Mama."
    ,"year": 2019,
    "reviews": []
},
{
    "id":7,
    "title":     "One Punch Man",
    "image": "https://cdn.myanimelist.net/images/anime/12/76049.jpg",
    "info":"The seemingly ordinary and unimpressive Saitama has a rather unique hobby: being a hero. In order to pursue his childhood dream, he trained relentlessly for three years—and lost all of his hair in the process. Now, Saitama is incredibly powerful, so much so that no enemy is able to defeat him in battle. In fact, all it takes to defeat evildoers with just one punch has led to an unexpected problem—he is no longer able to enjoy the thrill of battling and has become quite bored. This all changes with the arrival of Genos, a 19-year-old cyborg, who wishes to be Saitama's disciple after seeing what he is capable of. Genos proposes that the two join the Hero Association in order to become certified heroes that will be recognized for their positive contributions to society, and Saitama, shocked that no one knows who he is, quickly agrees. And thus begins the story of One Punch Man, an action-comedy that follows an eccentric individual who longs to fight strong enemies that can hopefully give him the excitement he once felt and just maybe, he'll become popular in the process."
    ,"year": 2015,
    "reviews": []
},
{
    "id":8,
    "title":     "Ashita no Joe 2",
    "image": "https://cdn.myanimelist.net/images/anime/3/45028.jpg",
    "info": "Yabuki Joe is left downhearted and hopeless after a certain tragic event. In attempt to put the past behind him, Joe leaves the gym behind and begins wandering. On his travels he comes across the likes of Wolf Kanagushi and Goromaki Gondo, men who unintentionally fan the dying embers inside him, leading him to putting his wanderings to an end. His return home puts Joe back on the path to boxing, but unknown to himself and his trainer, he now suffers deep-set issues holding him back from fighting. In attempt to quell those issues, Carlos Rivera, a world renowned boxer is invited from Venezuela to help Joe recover."
    ,"year": 1980,
    "reviews": []
},
{
    "id":9,
    "title":     "Mushishi Zoku Shou: Suzu no Shizuku",
    "image": "https://cdn.myanimelist.net/images/anime/9/72689.jpg",
    "info": "On a warm summer day, a boy heard the sound of bells ringing, as if in celebration, in the mountain near his home. Several years later in that same mountain, the mushishi Ginko encounters a strange girl with weeds growing out of her body. Soon after, Ginko coincidentally runs into the now grown-up boy Yoshiro on his way off the mountain. With Yoshiro’s help, Ginko soon begins to uncover who this mysterious girl is and what happened to her. An adaptation of the last arc in the manga, Mushishi Zoku Shou: Suzu no Shizuku follows Ginko’s peculiar journey amidst the occult to unravel the mystery behind the enigmatic girl called Kaya and the mountain that has become her home."
    ,"year": 2015,
    "reviews": []
},
{
    "id":10,
    "title":     "Kizumonogatari II: Nekketsu-hen",
    "image": "https://cdn.myanimelist.net/images/anime/1223/96541.jpg",
    "info": "After reverting to human from half-vampire, Koyomi Araragi decides to retrieve Kiss-shot Acerola-orion Heart-under-blade's severed body parts that were stolen by three powerful vampire hunters. Awaiting him are Dramaturgie, a vampire hunter who is a vampire himself; Episode, a half-vampire with the ability to transform into mist; and Guillotinecutter, a human priest who is the most dangerous of them all. Unbeknownst to Araragi, each minute he spends trying to retrieve Kiss-shot's limbs makes him less of a human and more of a vampire. Will he be able to keep his wish of becoming human once again by the end of his battles?"
    ,"year": 2016,
    "reviews": []
},
{
    "id":11,
    "title":     "Chihayafuru 3",
    "image": "https://cdn.myanimelist.net/images/anime/1590/102068.jpg",
    "info": "Winning the high school team tournament was a great accomplishment for the Mizusawa members. Each of them has made great strides in improving themselves, and the victory symbolizes how far they've come. But after accomplishing one goal, their individual aims are within reach. Chihaya Ayase has her sights set on Wakamiya Shinobu and the title of Queen, and now that Taichi Mashima has made it into Class A, he can finally compete against Arata Wataya. Everyone in Mizusawa wants to get better, and there's no telling what the future holds if they keep trying."
    ,"year": 2019,
    "reviews": []
},
{
    "id":12,
    "title":"Bakuman. 3rd Season",
    "image": "https://cdn.myanimelist.net/images/anime/6/41845.jpg",
    "info": "Onto their third serialization, manga duo Moritaka Mashiro and Akito Takagi—also known by their pen name, Muto Ashirogi—are ever closer to their dream of an anime adaption. However, the real challenge is only just beginning: if they are unable to compete with the artist Eiji Niizuma in the rankings within the span of six months, they will be canceled. To top it off, numerous rivals are close behind and declaring war. They don't even have enough time to spare thinking about an anime! In Bakuman. 3rd Season, Muto Ashirogi must find a way to stay atop the colossal mountain known as the Shounen Jack rankings. With new problems and new assistants, the pair continue to strive for their dream."
    ,"year": 2013,
    "reviews": []
},
{
    "id":13,
    "title":"Death Note",
    "image": "https://cdn.myanimelist.net/images/anime/9/9453.jpg",
    "info": "A shinigami, as a god of death, can kill any person—provided they see their victim's face and write their victim's name in a notebook called a Death Note. One day, Ryuk, bored by the shinigami lifestyle and interested in seeing how a human would use a Death Note, drops one into the human realm. High school student and prodigy Light Yagami stumbles upon the Death Note and—since he deplores the state of the world—tests the deadly notebook by writing a criminal's name in it. When the criminal dies immediately following his experiment with the Death Note, Light is greatly surprised and quickly recognizes how devastating the power that has fallen into his hands could be. With this divine capability, Light decides to extinguish all criminals in order to build a new world where crime does not exist and people worship him as a god. Police, however, quickly discover that a serial killer is targeting criminals and, consequently, try to apprehend the culprit. To do this, the Japanese investigators count on the assistance of the best detective in the world: a young and eccentric man known only by the name of L."
    ,"year": 2006,
    "reviews": []
},
{
    "id":14,
    "title":"Fate/Zero Season 2",
    "image": "https://cdn.myanimelist.net/images/anime/8/41125.jpg",
    "info": "As the Fourth Holy Grail War rages on with no clear victor in sight, the remaining Servants and their Masters are called upon by Church supervisor Risei Kotomine, in order to band together and confront an impending threat that could unravel the Grail War and bring about the destruction of Fuyuki City. The uneasy truce soon collapses as Masters demonstrate that they will do anything in their power, no matter how despicable, to win. Seeds of doubt are sown between Kiritsugu Emiya and Saber, his Servant, as their conflicting ideologies on heroism and chivalry clash. Meanwhile, an ominous bond forms between Kirei Kotomine, who still seeks to find his purpose in life, and one of the remaining Servants. As the countdown to the end of the war reaches zero, the cost of winning begins to blur the line between victory and defeat."
    ,"year": 2012,
    "reviews": []
},
{
    "id":15,
    "title":"Kimi no Na wa.",
    "image": "https://cdn.myanimelist.net/images/anime/5/87048.jpg",
    "info": "Mitsuha Miyamizu, a high school girl, yearns to live the life of a boy in the bustling city of Tokyo—a dream that stands in stark contrast to her present life in the countryside. Meanwhile in the city, Taki Tachibana lives a busy life as a high school student while juggling his part-time job and hopes for a future in architecture. One day, Mitsuha awakens in a room that is not her own and suddenly finds herself living the dream life in Tokyo—but in Taki's body! Elsewhere, Taki finds himself living Mitsuha's life in the humble countryside. In pursuit of an answer to this strange phenomenon, they begin to search for one another. Kimi no Na wa. revolves around Mitsuha and Taki's actions, which begin to have a dramatic impact on each other's lives, weaving them into a fabric held together by fate and circumstance."
    ,"year": 2016,
    "reviews": []
},
{
    "id":16,
    "title":"Gintama: Enchousen",
    "image": "https://cdn.myanimelist.net/images/anime/6/75172.jpg",
    "info": "While Gintoki Sakata was away, the Yorozuya found themselves a new leader: Kintoki, Gintoki's golden-haired doppelganger. In order to regain his former position, Gintoki will need the help of those around him, a troubling feat when no one can remember him! Between Kintoki and Gintoki, who will claim the throne as the main character? In addition, Yorozuya make a trip back down to red-light district of Yoshiwara to aid an elderly courtesan in her search for her long-lost lover. Although the district is no longer in chains beneath the earth's surface, the trio soon learn of the tragic backstories of Yoshiwara's inhabitants that still haunt them. With flashback after flashback, this quest has Yorozuya witnessing everlasting love and protecting it as best they can with their hearts and souls. Gintama': Enchousen includes moments of action-packed intensity along with their usual lighthearted, slapstick humor for Gintoki and his friends."
    ,"year": 2012,
    "reviews": []
},
{
    "id":17,
    "title":"A Silent Voice",
    "image": "https://cdn.myanimelist.net/images/anime/1122/96435.jpg",
    "info": "As a wild youth, elementary school student Shouya Ishida sought to beat boredom in the cruelest ways. When the deaf Shouko Nishimiya transfers into his class, Shouya and the rest of his class thoughtlessly bully her for fun. However, when her mother notifies the school, he is singled out and blamed for everything done to her. With Shouko transferring out of the school, Shouya is left at the mercy of his classmates. He is heartlessly ostracized all throughout elementary and middle school, while teachers turn a blind eye. Now in his third year of high school, Shouya is still plagued by his wrongdoings as a young boy. Sincerely regretting his past actions, he sets out on a journey of redemption: to meet Shouko once more and make amends. Koe no Katachi tells the heartwarming tale of Shouya's reunion with Shouko and his honest attempts to redeem himself, all while being continually haunted by the shadows of his past."
    ,"year": 2016,
    "reviews": []
},
{
    "id":18,
    "title":"Haikyu!! 3rd Season",
    "image": "https://cdn.myanimelist.net/images/anime/7/81992.jpg",
    "info": "After the victory against Aoba Jousai High, Karasuno High School, once called “a fallen powerhouse, a crow that can’t fly,” has finally reached the climax of the heated Spring tournament. Now, to advance to nationals, the Karasuno team has to defeat the powerhouse Shiratorizawa Academy. Karasuno’s greatest hurdle is their adversary’s ace, Wakatoshi Ushijima, the number one player in the Miyagi Prefecture, and one of the country’s top three aces. Only the strongest team will make it to the national tournament. Since this match is the third-year players’ last chance to qualify for nationals, Karasuno has to use everything they learned during the training camp and prior matches to attain victory. Filled with restlessness and excitement, both teams are determined to come out on top in the third season of Haikyuu!!."
    ,"year": 2016,
    "reviews": []
},
{
    "id":19,
    "title":"Clannad: After Story",
    "image": "https://cdn.myanimelist.net/images/anime/13/24647.jpg",
    "info": "Clannad: After Story, the sequel to the critically acclaimed slice-of-life series Clannad, begins after Tomoya Okazaki and Nagisa Furukawa graduate from high school. Together, they experience the emotional rollercoaster of growing up. Unable to decide on a course for his future, Tomoya learns the value of a strong work ethic and discovers the strength of Nagisa's support. Through the couple's dedication and unity of purpose, they push forward to confront their personal problems, deepen their old relationships, and create new bonds. Time also moves on in the Illusionary World. As the plains grow cold with the approach of winter, the Illusionary Girl and the Garbage Doll are presented with a difficult situation that reveals the World's true purpose. Based on the visual novel by Key and produced by Kyoto Animation, Clannad: After Story is an impactful drama highlighting the importance of family and the struggles of adulthood."
    ,"year": 2009,
    "reviews": []
},
{
    "id":20,
    "title":"Owarimonogatari Second Season",
    "image": "https://cdn.myanimelist.net/images/anime/6/87322.jpg",
    "info": "Following an encounter with oddity specialist Izuko Gaen, third-year high school student Koyomi Araragi wakes up in a strange, deserted void only to be greeted by a joyfully familiar face in an alarmingly unfamiliar place. Araragi, with the help of his girlfriend Hitagi Senjougahara, maneuvers through the webs of his past and the perplexities of the present in search of answers. However, fate once again delivers him to the eccentric transfer student Ougi Oshino, who brings forth an unexpected proposal that may unearth the very foundation to which he is anchored. As Araragi peels back the layers of mystery surrounding an apparition, he discovers a truth not meant to be revealed."
    ,"year": 2017,
    "reviews": []
},
{
    "id":21,
    "title":"Code Geass: Lelouch of the Rebellion R2",
    "image": "https://cdn.myanimelist.net/images/anime/4/9391.jpg",
    "info": "One year has passed since the Black Rebellion, a failed uprising against the Holy Britannian Empire led by the masked vigilante Zero, who is now missing. At a loss without their revolutionary leader, Area 11's resistance group—the Black Knights—find themselves too powerless to combat the brutality inflicted upon the Elevens by Britannia, which has increased significantly in order to crush any hope of a future revolt. Lelouch Lamperouge, having lost all memory of his double life, is living peacefully alongside his friends as a high school student at Ashford Academy. His former partner C.C., unable to accept this turn of events, takes it upon herself to remind him of his past purpose, hoping that the mastermind Zero will rise once again to finish what he started, in this thrilling conclusion to the series."
    ,"year": 2008,
    "reviews": []
},
{
    "id":22,
    "title":"Mob Psycho 100 II",
    "image": "https://cdn.myanimelist.net/images/anime/1918/96303.jpg",
    "info": "Shigeo Mob Kageyama is now maturing and understanding his role as a supernatural psychic that has the power to drastically affect the livelihood of others. He and his mentor Reigen Arataka continue to deal with supernatural requests from clients, whether it be exorcizing evil spirits or tackling urban legends that haunt the citizens. While the workflow remains the same, Mob isn't just blindly following Reigen around anymore. With all his experiences as a ridiculously strong psychic, Mob's supernatural adventures now have more weight to them. Things take on a serious and darker tone as the dangers Mob and Reigen face are much more tangible and unsettling than ever before."
    ,"year": 2019,
    "reviews": []
},
{
    "id":23,
    "title":"Spirited Away",
    "image": "https://cdn.myanimelist.net/images/anime/6/79597.jpg",
    "info": "Stubborn, spoiled, and naïve, 10-year-old Chihiro Ogino is less than pleased when she and her parents discover an abandoned amusement park on the way to their new house. Cautiously venturing inside, she realizes that there is more to this place than meets the eye, as strange things begin to happen once dusk falls. Ghostly apparitions and food that turns her parents into pigs are just the start—Chihiro has unwittingly crossed over into the spirit world. Now trapped, she must summon the courage to live and work amongst spirits, with the help of the enigmatic Haku and the cast of unique characters she meets along the way. Vivid and intriguing, Sen to Chihiro no Kamikakushi tells the story of Chihiro's journey through an unfamiliar world as she strives to save her parents and return home."
    ,"year": 2001,
    "reviews": []
},
{
    "id":24,
    "title":"Demon Slayer: Kimetsu no Yaiba",
    "image": "https://cdn.myanimelist.net/images/anime/1286/99889.jpg",
    "info": "Ever since the death of his father, the burden of supporting the family has fallen upon Tanjirou Kamado's shoulders. Though living impoverished on a remote mountain, the Kamado family are able to enjoy a relatively peaceful and happy life. One day, Tanjirou decides to go down to the local village to make a little money selling charcoal. On his way back, night falls, forcing Tanjirou to take shelter in the house of a strange man, who warns him of the existence of flesh-eating demons that lurk in the woods at night. When he finally arrives back home the next day, he is met with a horrifying sight—his whole family has been slaughtered. Worse still, the sole survivor is his sister Nezuko, who has been turned into a bloodthirsty demon. Consumed by rage and hatred, Tanjirou swears to avenge his family and stay by his only remaining sibling. Alongside the mysterious group calling themselves the Demon Slayer Corps, Tanjirou will do whatever it takes to slay the demons and protect the remnants of his beloved sister's humanity."
    ,"year": 2019,
    "reviews": []
},
{
    "id":25,
    "title":"Your Lie in April",
    "image": "https://cdn.myanimelist.net/images/anime/3/67177.jpg",
    "info": "Music accompanies the path of the human metronome, the prodigious pianist Kousei Arima. But after the passing of his mother, Saki Arima, Kousei falls into a downward spiral, rendering him unable to hear the sound of his own piano. Two years later, Kousei still avoids the piano, leaving behind his admirers and rivals, and lives a colorless life alongside his friends Tsubaki Sawabe and Ryouta Watari. However, everything changes when he meets a beautiful violinist, Kaori Miyazono, who stirs up his world and sets him on a journey to face music again. Based on the manga series of the same name, Shigatsu wa Kimi no Uso approaches the story of Kousei's recovery as he discovers that music is more than playing each note perfectly, and a single melody can bring in the fresh spring air of April."
    ,"year": 2015,
    "reviews": []
},
{
    "id":26,
    "title":"Made in Abyss",
    "image": "https://cdn.myanimelist.net/images/anime/6/86733.jpg",
    "info": "The Abyss—a gaping chasm stretching down into the depths of the earth, filled with mysterious creatures and relics from a time long past. How did it come to be? What lies at the bottom? Countless brave individuals, known as Divers, have sought to solve these mysteries of the Abyss, fearlessly descending into its darkest realms. The best and bravest of the Divers, the White Whistles, are hailed as legends by those who remain on the surface. Riko, daughter of the missing White Whistle Lyza the Annihilator, aspires to become like her mother and explore the furthest reaches of the Abyss. However, just a novice Red Whistle herself, she is only permitted to roam its most upper layer. Even so, Riko has a chance encounter with a mysterious robot with the appearance of an ordinary young boy. She comes to name him Reg, and he has no recollection of the events preceding his discovery. Certain that the technology to create Reg must come from deep within the Abyss, the two decide to venture forth into the chasm to recover his memories and see the bottom of the great pit with their own eyes. However, they know not of the harsh reality that is the true existence of the Abyss."
    ,"year": 2017,
    "reviews": []
},
{
    "id":27,
    "title":"Cowboy Bebop",
    "image": "https://cdn.myanimelist.net/images/anime/4/19644.jpg",
    "info": "In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as Cowboys. The ragtag team aboard the spaceship Bebop are two such individuals. Mellow and carefree Spike Spiegel is balanced by his boisterous, pragmatic partner Jet Black as the pair makes a living chasing bounties and collecting rewards. Thrown off course by the addition of new members that they meet in their travels—Ein, a genetically engineered, highly intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic trickster with memory loss; and the strange computer whiz kid Edward Wong—the crew embarks on thrilling adventures that unravel each member's dark and mysterious past little by little. Well-balanced with high density action and light-hearted comedy, Cowboy Bebop is a space Western classic and an homage to the smooth and improvised music it is named after."
    ,"year": 1998,
    "reviews": []
},
{
    "id":28,
    "title":"Vinland Saga",
    "image": "https://cdn.myanimelist.net/images/anime/1500/103005.jpg",
    "info": "Young Thorfinn grew up listening to the stories of old sailors that had traveled the ocean and reached the place of legend, Vinland. It's said to be warm and fertile, a place where there would be no need for fighting—not at all like the frozen village in Iceland where he was born, and certainly not like his current life as a mercenary. War is his home now. Though his father once told him, You have no enemies, nobody does. There is nobody who it's okay to hurt, as he grew, Thorfinn knew that nothing was further from the truth. The war between England and the Danes grows worse with each passing year. Death has become commonplace, and the viking mercenaries are loving every moment of it. Allying with either side will cause a massive swing in the balance of power, and the vikings are happy to make names for themselves and take any spoils they earn along the way. Among the chaos, Thorfinn must take his revenge and kill the man who murdered his father, Askeladd. The only paradise for the vikings, it seems, is the era of war and death that rages on."
    ,"year": 2019,
    "reviews": []
},
{
    "id":29,
    "title":"Princess Mononoke",
    "image": "https://cdn.myanimelist.net/images/anime/7/75919.jpg",
    "info": "When an Emishi village is attacked by a fierce demon boar, the young prince Ashitaka puts his life at stake to defend his tribe. With its dying breath, the beast curses the prince's arm, granting him demonic powers while gradually siphoning his life away. Instructed by the village elders to travel westward for a cure, Ashitaka arrives at Tatara, the Iron Town, where he finds himself embroiled in a fierce conflict: Lady Eboshi of Tatara, promoting constant deforestation, stands against Princess San and the sacred spirits of the forest, who are furious at the destruction brought by the humans. As the opposing forces of nature and mankind begin to clash in a desperate struggle for survival, Ashitaka attempts to seek harmony between the two, all the while battling the latent demon inside of him. Princess Mononoke is a tale depicting the connection of technology and nature, while showing the path to harmony that could be achieved by mutual acceptance."
    ,"year": 1997,
    "reviews": []
},
{
    "id":30,
    "title":"Dragon Ball Z",
    "image": "https://cdn.myanimelist.net/images/anime/6/20936.jpg",
    "info": "Five years after winning the World Martial Arts tournament, Gokuu is now living a peaceful life with his wife and son. This changes, however, with the arrival of a mysterious enemy named Raditz who presents himself as Gokuu's long-lost brother. He reveals that Gokuu is a warrior from the once powerful but now virtually extinct Saiyan race, whose homeworld was completely annihilated. When he was sent to Earth as a baby, Gokuu's sole purpose was to conquer and destroy the planet; but after suffering amnesia from a head injury, his violent and savage nature changed, and instead was raised as a kind and well-mannered boy, now fighting to protect others. With his failed attempt at forcibly recruiting Gokuu as an ally, Raditz warns Gokuu's friends of a new threat that's rapidly approaching Earth—one that could plunge Earth into an intergalactic conflict and cause the heavens themselves to shake. A war will be fought over the seven mystical dragon balls, and only the strongest will survive in Dragon Ball Z."
    ,"year": 1989,
    "reviews": []
},
    {
    "id":31,
    "title": "Naruto",
    "image": "https://cdn.myanimelist.net/images/anime/13/17405.jpg",
    "info": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.Now, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.",
    "year": 2002,
    "reviews": [["I loved Naruto",False], ["Naruto was okay",False], ["wasn't the biggest fan",False], ["Yah are bugging, naruto is amazing",False]]
},

]

#animeList=['Naruto', 'Hunter x Hunter', 'Fullmetal Alchemist: Brotherhood', 'Bleach', 'Suzumiya Haruhi no Shoushitsu', 'Yakusoku no Neverland', 'One Punch Man', 'Ashita no Joe 2', 'Mushishi Zoku Shou: Suzu no Shizuku', 'Kizumonogatari II: Nekketsu-hen', 'Chihayafuru 3', 'Bakuman. 3rd Season', 'Death Note', 'Fate/Zero Season 2', 'Kimi no Na wa.', 'Gintama: Enchousen', 'A Silent Voice', 'Haikyu!! 3rd Season', 'Clannad: After Story', 'Owarimonogatari Second Season', 'Code Geass: Lelouch of the Rebellion R2', 'Mob Psycho 100 II', 'Spirited Away', 'Demon Slayer: Kimetsu no Yaiba', 'Your Lie in April', 'Made in Abyss', 'Cowboy Bebop', 'Vinland Saga', 'Princess Mononoke', 'Dragon Ball Z']

current_id = 32


@app.route('/')
def animeHomeLoad():
    return "Hello bro"
    return render_template('anime.html', cards=animeInfo[-9:]) 

@app.route('/view/<id>')
def view(id=None):
    print(f'Look id is {id}')
    look=int(id)
    temp={
    "id":look,
    "title":     "",
    "image": "",
    "info":""
    ,"year": 0,
    "reviews": ["Error"]
}
    for i in animeInfo:
        if i["id"]==look:
            temp["title"]=i["title"]
            temp["image"]=i["image"]
            temp["info"]=i["info"]
            temp["year"]=i["year"]
            temp["reviews"]=i["reviews"]
    
    return render_template('view.html',id=look,currentAnime=temp) 

@app.route('/search', methods=['GET', 'POST'])
def update():
    global animeInfo
    json_data = request.get_json() 
    #print(json_data)
    #print(f'Searching for {json_data} and of type {type(json_data)}') 
    requestList=[]
    pat=json_data
    for i in animeInfo:
        if re.search(pat.lower(),i["title"].lower())!=None:
            result = re.sub('('+pat.lower()+')', r'<b>\1</b>', i["title"],flags=re.IGNORECASE)  
            bob={
               "id":i["id"],
                "title":     result,
                "image": i["image"],
                "info":i["info"]
                ,"year": i["year"],
                "reviews": i["reviews"]
            }
            requestList.append(bob)
        elif re.search(pat.lower(),i["info"].lower())!=None:
            #result = re.sub('('+pat.lower()+')', r'<b>\1</b>', i["info"],flags=re.IGNORECASE)  
            requestList.append(i)            
    return jsonify(requestList=requestList) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    global animeInfo
    #0 means none, 1 means review only, 2 means dateONLY, 3 means both
    json_data=request.get_json() 
    print(f'-----------{json_data}')
    if json_data["combo"]==1:
        look = json_data["id"]
        review = json_data["review"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["reviews"].append([review,False])
        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1
    elif json_data["combo"]==2:
        look = json_data["id"]
        date = json_data["year"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["year"]=int(date)
        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1
    elif json_data["combo"]==3:
        look = json_data["id"]
        review = json_data["review"]
        date = json_data["year"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["reviews"].append([review,False])
        animeInfo[lookIndex]["year"]=int(date)

        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1

    else:
        return jsonify(id="look")
@app.route('/undo', methods=['GET', 'POST'])
def undo():
    global animeInfo
#   global animeList
    json_data = request.get_json() #Usually json_data would be just an int, now it is a list where first is int and second is location of review to mark as true 
    reviewList=[]
    print(json_data)
    #Found possible Issue: It is i am not deleting
    for i in range(len(animeInfo)):
        if animeInfo[i]["id"]==json_data[0]:
            for k in range(len(animeInfo[i]["reviews"])):
                if k == json_data[1]:
                    animeInfo[i]["reviews"][k][1]=False
                    reviewList=animeInfo[i]["reviews"]
                    break
            break
    return jsonify(reviewList=reviewList)



@app.route('/delete_review', methods=['GET', 'POST'])
def delete_review():
    global animeInfo
#   global animeList
    json_data = request.get_json() #Usually json_data would be just an int, now it is a list where first is int and second is location of review to mark as true 
    reviewList=[]
    print(json_data)
    #Found possible Issue: It is i am not deleting
    for i in range(len(animeInfo)):
        if animeInfo[i]["id"]==json_data[0]:
            for k in range(len(animeInfo[i]["reviews"])):
                if k == json_data[1]:
                    animeInfo[i]["reviews"][k][1]=True
                    reviewList=animeInfo[i]["reviews"]
                    break
            break
    return jsonify(reviewList=reviewList) 
@app.route('/create')
def create():
    return render_template('create.html',current_id=current_id) 

@app.route('/add_anime', methods=['GET', 'POST'])
def add_anime():
    global animeInfo
    global current_id
    json_data = request.get_json()
    print(f"Requesting {json_data}")
    animeInfo.append(json_data)
    current_id+=1
    return jsonify(lastID=(current_id-1)) 
if __name__ == '__main__':
   app.run(debug = True)



