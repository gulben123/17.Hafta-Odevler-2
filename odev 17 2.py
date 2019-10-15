import sqlite3

menu=""" Baskent sorgulamak icin 1'e,
Bolgede konusulan tum diller icin 2'ye,
Bir dilin konusuldugu tum sehirlerin sayisi icin 3'e,
Bir dilin hangi bolgede hangi ulkelerde konusuldugunu gormek icin 4'e,
Tum kitalarda hangi dillerin konusuldugunu gormek icin 5'e basiniz. """
data=sqlite3.connect('world.db')
im=data.cursor()
print(menu)
while True:
    choose=input("Lutfen seciminizi tuslayiniz: ")
    if choose=='1':
        question1=input(" Hangi ulkenin baskentini ogrenmek istiyorsunuz: ")
        im.execute("""SELECT capital FROM country WHERE name=?""")
        question1=im.fetchone()
        for i in question1:
            print(question1)
    elif choose== '2':
        question2=input("Hangi bolgede konusulan dilleri ogrenmek istiyorsunuz: ")
        im.execute("""SELECT countrylanguage.language FROM countrylanguage INNER JOIN country WHERE region = ? """)
        question2=im.fetchall()
        for i in question2:
            print(question2)
    elif choose == '3':
        question3= input("Hangi dilin kac farkli bolgede konusuldugunu ogrenmek istersiniz: ")
        im.execute("""SELECT city.name FROM city INNER JOIN countrylanguage ON countrylanguage.countrycode=city.country WHERE language =?""")
        question3=im.fetchall()
        for i in question3:
            print (question3)
    elif choose=='4':
        region1=input("Bolgenin ismini giriniz: ")
        language1=input("Bir dil giriniz: ")
        im.execute("""SELECT countrylanguage.country FROM country WHERE language=? AND region=?""")
        country=im.fetchall()
        for i in country:
            print(country)
    elif choose=='5':
        im.execute("""SELECT country.contitent FROM countrylanguage  WHERE country.code=countrylanguage.countrycode""")
        contitent=im.fetchall()
        for i in contitent:
            print(contitent)
            
            
