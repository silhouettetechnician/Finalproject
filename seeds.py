from app import app, db
from models.itemPost import ItemPost, Comment
from models.category import Category
from models.designer import Designer
from models.user import UserSchema
user_schema = UserSchema()
# pylint: disable=E1101
with app.app_context():
    db.drop_all()
    db.create_all()

    Michael, errors = user_schema.load({
        'name': 'Micheal Jordan',
        'username': 'Michaelj',
        'email': 'mikey@email.com',
        'image': 'http://www.leisureopportunities.com/images/995586_746594.jpg',
        'password': 'm123',
        'password_confirmation': 'm123',
        'discounts': 'Selfridges(40%)',
        'brand_likes': 'Axel Arigato'
        })

    if errors:
        raise Exception(errors)



    Tommy, errors = user_schema.load({
        'name': 'Martina Jones',
        'username': 'Tina89',
        'email': 'martina@email.com',
        'image': "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample4.jpg",
        'password': 't123',
        'password_confirmation': 't123',
        'discounts': 'Moncler(60%)',
        'brand_likes': 'John Smedley'
        })

    if errors:
        raise Exception(errors)

    Marian, errors = user_schema.load({
        'name': 'Marian Obrien',
        'username': 'Marian_O',
        'email': 'marian.obrien70@example.com',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Amber%27sDuckFace.jpg',
        'password': 'marian1',
        'password_confirmation': 'marian1',
        'discounts': 'Ralph Lauren(30%)',
        'brand_likes': 'Chanel'
        })

    if errors:
        raise Exception(errors)

    Joe, errors = user_schema.load({
        'name': 'Joseph Hobbs',
        'username': 'eastebay',
        'email': 'joe@email.com',
        'image': "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample5.jpg",
        'password': 'j123',
        'password_confirmation': 'j123',
        'discounts': 'Nike(n/a)',
        'brand_likes': 'Rick Owens'
        })

    if errors:
        raise Exception(errors)

    Marilyn, errors = user_schema.load({
        'name': 'Marilyn Salinas',
        'username': 'pebblecross',
        'email': 'marilyn@email.com',
        'image': "https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample6.jpg",
        'password': 'ma123',
        'password_confirmation': 'ma123',
        'discounts': 'Nike(40%)',
        'brand_likes': 'Burberry'
        })

    if errors:
        raise Exception(errors)




# ************************  CATEGORIES ***************************

    Clothing = Category(name='Clothing')
    Shoes = Category(name='Shoes')
    Accessories = Category(name='Accessories')

        # ****************Designers*******************

    Saint_Laurent = Designer(name='Saint Laurent', image='https://en.parisinfo.com/var/otcp/sites/images/node_43/node_51/node_77884/node_77893/saint-laurent-paris-%7C-630x405-%7C-%C2%A9-dr/10970960-1-fre-FR/Saint-Laurent-Paris-%7C-630x405-%7C-%C2%A9-DR.jpg')
    Gucci = Designer(name='Gucci', image='https://cdn.shopify.com/s/files/1/2374/3709/products/GUCCI_THUMB_237af47c-c672-444b-bd49-5bf9b5d4b99b_2048x2048.jpg?v=1514073359')
    Givenchy = Designer(name='Givenchy', image='http://bbwbettiepumpkin.com/wp-content/uploads/2019/01/givenchy-logo-givenchy-paris-givenchy-paris-tapestry-teepublic-printable.jpg')
    Common_Projects = Designer(name='Common Projects', image='https://storage.googleapis.com/stateless-cavour/2018/05/91a2ddc3-common.jpg')
    Comme_De_Garcons = Designer(name='Comme De Garcons', image='https://vignette.wikia.nocookie.net/iamamiwhoami/images/9/95/COMME_des_GAR%C3%87ONS_logo.jpg/revision/latest?cb=20171122055157')
    Acne_Studios = Designer(name='Acne Studios', image='https://yt3.ggpht.com/a-/AAuE7mBM37SRyjhFlewWQF-QPILe6iK9EsoK7oOnSA=s900-mo-c-c0xffffffff-rj-k-no')
    Alexaner_Wang = Designer(name='Alexander Wang', image='https://www.dfs.com/medias/Alexander-Wang-Brand-Logo-Bottom-en.jpeg-en-340x340.jpg?context=bWFzdGVyfEJSQU5EX01FRElBfDQ5Mjl8aW1hZ2UvanBlZ3wvbWVkaWEvaW1hZ2UvYnJhbmQvaDA3L2hiNS84ODE0NzQ2NjY0OTkwLmpwZ3xhZWVmMDg0YTU4NDg5MzlmNDA2NzMyNzNiMDc5MmQ0ZmI2NzcyMzRkZmFjZjliMzNkMmFlZTU0N2UwNmUyY2Qx')
    Adidas = Designer(name='Adidas', image='https://cdn.shopify.com/s/files/1/2374/3709/products/ADIDAS_THUMB_394x.jpg?v=1513997993')
    Moncler = Designer(name='Moncler', image='https://www.flannels.com/images/marketing/moncler-brand-banner-260118.jpg')
    Burberry = Designer(name='Burberry', image='https://www.instagram.com/p/Bl-VwDsHVvP/media/?size=l')
    Balenciaga = Designer(name='Balenciaga', image='https://www.paragon.com.sg/media/1/stores/b/balenciaga_feature.jpg')
    Prada = Designer(name='Prada', image='https://i.etsystatic.com/16659961/d/il/b72dd3/1672223002/il_340x270.1672223002_7t80.jpg?version=0')
    Trickers = Designer(name='Tricker', image='https://static1.squarespace.com/static/55167579e4b0fd1c92d5857f/t/5a9b214bf9619a4498345b06/1552600891711/trickers+shoes+logo.png')
    Supreme = Designer(name='Supreme', image='https://cdn.shopify.com/s/files/1/0866/4890/products/supreme-sticker_1024x1024.jpg?v=1535013742')
    Maison_Margiela = Designer(name='Maison Margiela', image='https://upload.wikimedia.org/wikipedia/commons/9/99/Maison_margiela-corporate_logo_2015.jpg')
    Off_White = Designer(name='Off White', image='https://ih0.redbubble.net/image.417864596.0577/raf,750x1000,075,t,fafafa:ca443f4786.jpg')
    Nike = Designer(name='Nike', image='http://cdn.shopify.com/s/files/1/1636/0487/products/300115_grande.jpg?v=1500049799')
    Palace = Designer(name='Palace', image='https://cdn.shopify.com/s/files/1/2374/3709/products/PALACE_THUMB_557d4084-cd3e-4db5-bf4b-f2207f3613c4_394x.jpg?v=1514004812')
    Issey_Miyake = Designer(name='Issey Miyake', image='https://www.franks.com.mt/wp-content/uploads/2016/06/Issey-Miyake-Logo.jpg')
    Rick_Owens = Designer(name='Rick Owens', image='https://cdn.shopify.com/s/files/1/0383/4289/collections/Rick-owens_1024x1024.jpg?v=1498780605')
    Chanel = Designer(name='Chanel', image='https://i.pinimg.com/originals/f9/57/f1/f957f1ed167de560fcadfc6a228e7f2e.jpg')

        # **********************POSTS**********************

    postone = ItemPost(creator=Tommy, title='Light Blue D2 Distressed Slim Jeans', description="""Distressed Slim Jeans from FW16
    Skinny fit, Low rise Tagged 34, fit 36. Looking to purchase these with a discount, if anyone can help please check out my account, i'm, willing to share with the brands ive posted""", size='Small', designers=[Gucci], categories=[Clothing], image1=
    'https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/ddr1pIo7QNCcwfzPjmSA', image2='https://i.pinimg.com/originals/bb/17/ce/bb17cee2b712dffdec0a3ace35189964.jpg')

    posttwo = ItemPost(creator=Joe, title='Ribbed Virgin Wool Beanie', description="""Authentic MONCLER GRENOBLE Ribbed Virgin Wool Beanie from FW'18/19""", size='One_Size', designers=[Moncler], categories=[Accessories], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/437phQQzmtUDsFKxRf0Q', image2='https://i.pinimg.com/originals/bb/17/ce/bb17cee2b712dffdec0a3ace35189964.jpg')

    postthree = ItemPost( creator=Tommy, title='Men\'s Gray Skinny Fit Double Breasted Herringbone Blazer', description="""100% Authentic Burberry Prorsum Men's Grey Skinny Fit Double Breasted Herringbone Blazer from FW'11/12""", designers=[Burberry], categories=[Clothing], size="""shoulder - 17,3' / 44 cm, length - 29,1' / 74, arm - 25,8""", image1='https://www.essentialstyleformen.com/wp-content/uploads/2012/08/Burberry_Skinny_Fit_Double_Breasted_Herringbone_Jacket1.jpg', image2='https://i.pinimg.com/originals/bb/17/ce/bb17cee2b712dffdec0a3ace35189964.jpg')

    postfour = ItemPost(creator=Marilyn, title='NWT York Pale Pink SS17', description="""NWT Size 44/XS-S Hazel Beige Retail $240 Fits oversize""", size="""15.5" neck (39.4 cm) 20.25" chest (51.4 cm) 18" shoulder to shoulder (45.7 cm) 35.25" sleeve length (89.4 cm) 28.5" front length (72.4 cm)""", designers=[Acne_Studios], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/FddkIBOlRcA4vGsBKhH0', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/6SpN7pSQIbArcLDYOWzA')

    postfive = ItemPost(creator=Joe, title='BNWT Adidas x Alexander Wang Track Pants', description="""Limited edition Alexander Wang collaboration Track Pants, I'm looking for the best discount i can get, check out my profile for swaps""", size="""Size: US 30 / EU 46""", designers=[Alexaner_Wang, Adidas], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/D9pg5o8ITOu1CcHIGaEm', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/Km0c6tRbROGQUQODDI5F', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/lhUY9bE3Q9GThW9tnuoQ')

    postsix = ItemPost(creator=Tommy, title='Gucci Angry Cat Sweater', description="""Gucci sweater needed asap, will offer discount or more than willing to pay in bank transfer please check out my account and let me know""", size="""Size: US L / EU 52-54 / 3""", designers=[Gucci], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/9ZcCFr6QuQpAuomBAuSg', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/6gNEHlZ6QO55eUGFluxW', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/l3maRxdnQT688GV1bnw6')

    postseven = ItemPost(creator=Joe, title='Common Projects Achilles Low White Leather', description="""White Common Projects low sneakers wanted, willing to offer a discount swap if you're interested in my discount list""", size="""Size: US 7 / EU 40""", designers=[Common_Projects], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/XiCwwe5T4mhmvwhY87nA', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PC055GAqQs6ER9dsAb0R', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WB8iYuuRwij2VcVuoTfM')

    posteight = ItemPost(creator=Michael, title='Jacket Yellow x Red multi-color bore coat button up patch pocket nylon cotton', description="""- 100% authentic or money back. Let me know if you have any question before you order. Ships quickly by EMS(International Express Mail Service) with Tracking number. Ship from Japan.""", size="""Shoulder width:15.7 Width(pit to pit):19.7Front body(back neck-point to bottom):28.9Sleeve(from center neck to sleeve edge):26.4""", designers=[Prada], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/XiCwwe5T4mhmvwhY87nA', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PC055GAqQs6ER9dsAb0R', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WB8iYuuRwij2VcVuoTfM')

    postnine= ItemPost(creator=Joe, title='Rare Check Burberry pants', description="""I find these trocreators sublime, please  if anyone can help me get this for a good price, im sure i can help you out.""", size="""Size: US 8 / EU 41""", designers=[Burberry], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/NoDrCuicQUKAykZSH1qc', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/99bTgFd4Spe3605HfBQu', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/T9xULJsSayXIyDCSf1hs')

    postten= ItemPost(creator=Marilyn, title='Tricker’s Lambourn Jodphur NWT', description="""Nwt Trickers boots Lambourn size 8US. Made in England by the oldest shoemakers since 1829. Retail price $600 USD. New with tag, original box, cleaning cloth, fabric bag and original aftercare document.""", size="""Size: US 7 / EU 40""", designers=[Trickers], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/iIb7vlDOQYec9jTAe6GS', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WvphjW4DSRGAQE8MBUSF', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/pXK3bNxTQVSebkfMJOXP')

    posteleven = ItemPost(creator=Marian, title='GIVENCHY CURB CHAIN BRACELET', description=""" Gold plated stainless steel Givenchy curb chain bracelet from the Ricardo Tisci era. Worn well but still has a lot of life. The plating is wearing off on certain parts of the bracelet. Chain link measures 5/8" wide and it is 8" long from end to end.""", size="""5/8" wide and it is 8" long from end to end.""", designers=[Givenchy], categories=[Accessories], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/28kc5N9oTK2je2p43oEl', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/yJnZOvwHTz2HYAmbdhk3', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/nCOc6nMRQCS64FV0l9LA')


    posttwelve = ItemPost(creator=Joe, title='SUPREME × COMME DES GARCONS', description="""Comme de Garcons hoodie, really want please help me with discount someone.""", size="""Size: US M / EU 48-50 / 2""", designers=[Supreme], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/jjaNWe7RZKtzDf54LZTh', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/qORyB2k4R0yl0T2BuO4o', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/2spOLj5lTsiogofPiUkq')


    postthirteen = ItemPost(creator=Tommy, title='Maison Margiela Coat', description="""ive been looking for this coat for years. Really not up for paying full price, can anyone help me?""", size="""Size: US M / EU 48-50 / 2""", designers=[Maison_Margiela], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/5SDffkT6TKmSohzJnKog', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WsCcfjZYQja5EyHjJoDI', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/BGo9GSmVS02Ztirnu1pr')


    postfourteen = ItemPost(creator=Marian, title='Off-White Converse', description="""Off-White collaboration with Converse SS19. I've wanted these trainers for at least a year, i have good contacts at most high luxury retailers""", size="""Size: US 10 / EU 43""", designers=[Common_Projects], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PWkdbNONRLCoKJ36Xtlr', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/hIkCHV90STa3jrrw7tEK', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/KaXP8IiMTUmI5C52c9ve')


    postfifteen = ItemPost(creator=Tommy, title='Supreme Playboy Soccer Jersey Red L', description="""My cousin is desperate for this sweater, i'm not quite willing to buy it full price, I have a discount at Harrods, if you get in contact, im sure we can help each other""", size="""Size: US L / EU 52-54 / 3""", designers=[Supreme], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/v4WGLKteT3WJT4RVAbso')


    postsixteen = ItemPost(creator=Joe, title='SS14 Supreme Aspen Warm Up Pants', description="""White Common Projects low sneakers wanted, willing to offer a discount swap if you're interested in my discount list""", size="""Size: US 7 / EU 40""", designers=[Common_Projects], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/XiCwwe5T4mhmvwhY87nA', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PC055GAqQs6ER9dsAb0R', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WB8iYuuRwij2VcVuoTfM')


    postseventeen = ItemPost(creator=Michael, title='Air Force 1 Miami Vice Natural Linen Canvas', description="""VICE NATURAL LINEN CANVAS Comes with OG Box and extra white laces. Beautiful shoe""", size="""Size: US 9.5 / EU 42-43""", designers=[Nike], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/rMRruwgcT5OISNQlpbZd', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/iVqnXXfTgyIL79gtKQ3w', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PsaqZiuRfCh0FHqca2wO')


    posteighteen = ItemPost(creator=Marian, title='Palace Lazer Hood', description="""Made with Polartec technology: "Warmth without weight, highly breathable, pill-resistant, fast drying, durable, easy care". Orange color way.""", size="""Size XL. Fits like a Large""", designers=[Palace], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/Kj4muINQoWWL2QX1lf0U', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/jZ5HcJUfTqW0Y2c2GDuc', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/CicHRBPSAqEbfM6YsGDM')


    postnineteen = ItemPost(creator=Joe, title='Signature GG Leather Belt', description="""Condition: Brand New, with tags, dustbag. Retail price: $450 Season: 2019, permanent collection Designer: Gucci Color: Black, silver palladium hardware Disclaimer: Payment only through Grailed!""", size="""Size: 34""", designers=[Gucci], categories=[Accessories], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/H2IRYSE5S8O2uHzpOMdj', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/55MvXp2xSVi4zBda4uU1', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/eWvzxI8vRISY3MWywFXK')


    posttwenty = ItemPost(creator=Joe, title="""NIKE × OFF-WHITE × VIRGIL ABLOH Nike Off White Blazer All Hallows""", description="""Been looking for these shoes at a discounted price for ages, if anyone can help please message me""", size="""Size 11""", designers=[Off_White], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/yS9QRnigSCOZnXdZQfLx', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/Ibj5yYUTSr6TPiClnU2R', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/3HPSFhzSiCbVwto6qf0V')


    posttwentyone = ItemPost(creator=Michael, title='Homme Plisse Issey Miyake Hoodie', description="""Need this hoodie, message for details""", size="""Size: US M / EU 48-50 / 2""", designers=[Issey_Miyake], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/CtRXvL0TTKOLf9s8bmbN', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/WZUqOxUfSi2zMQM1tRe6')


    posttwentytwo = ItemPost(creator=Joe, title='Rare Anthem S/S 11 Mollino Multi-Material Jacket', description="""This is one of the few examples i’ve ever come across that features the tight knitted sleeves in the mens jackets. These are usually only in womens jackets""", size="""Size: US M / EU 48-50 / 2""", designers=[Rick_Owens], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/wQA77l9dSZKin78IKpun', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/ddTz6yafQfqQgB5J7Dbk', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/3xelM8v8T2uGhYZw2DiA')


    posttwentythree = ItemPost(creator=Michael, title='Air Force 1 Low Off-White Volt', description="""needed these the second they dropped. Check my account for swap details etc, message me for the best price you can give""", size="""Size 13""", designers=[Off_White, Nike], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/0IrEu2u8SiKvbuTBvYIC', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/ivBrqGQISgyGa8kw4pxP', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/E2JlE94TKwfXzhObzf0w')


    posttwentyfour = ItemPost(creator=Joe, title='2018 Chanel furry sneakers', description="""I work at Gucci and can get anyone a big discount, if you have these shoes at a lower price, get in contact""", size="""Size: US 7 / EU 40""", designers=[Chanel], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/ejAdJMVSlqNLsXhwLG2A', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/wrhI4HdpRBmyfppd9TWz')


    posttwentyfive= ItemPost(creator=Michael, title='New! Wmns AW18 Alpaca coat', description="""Rick Owned AW18 unbelievably soft alpaca mix yellow/ raisin checked coat. Women’s but totally unisex""", size="""Size 42 fits up to men’s slim large """, designers=[Rick_Owens], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/DPiiD4EdRQS4TByncDp2', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/jZxLE4Q3REu5YdEZJbbr', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/7DWpx3L8T0rQ8Gp00vRE')


    posttwentysix = ItemPost(creator=Joe, title='Black Creatch Cargo Pants', description="""There is nothing that id want more than these cargo pants, I have asked my parents to buy them for my birthday but i'd appreciate a discount""", size="""Size: US 32 / EU 48""", designers=[Rick_Owens], categories=[Clothing], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/iXb4f2SETAC609Mhi76K', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/taEZ6sh5Qu6yTReqN0aT', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/afSsjZlpQua0Ahae8V7Z')


    posttwentyseven = ItemPost(creator=Tommy, title='BALENCIAGA TRIPLE S size 9(42Eu) multicolor', description="""I know these are very common but i just love them!""", size="""Size: US 9 / EU 42""", designers=[Balenciaga], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/PDYpCL7AS9LgyqPUA4cA', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/F4Gg4aOtRHeSqPsRiSqt', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/MMyCqDnCSvCnlGdCfNHW')

    posttwentyeight = ItemPost(creator=Joe, title='RARE Saint Laurent Chain Wyatt fw13', description="""The most popular boots around, need these badly. please help. will pay anything""", size="""Size: US 8.5 / EU 41-42""", designers=[Saint_Laurent], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/2acswKZbR8KkOKV6t5lL', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/AiYi3ph5SQC4GhRzTJjz', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/mW5LENnvThSNHaDWyRzP')

    posttwentynine = ItemPost(creator=Tommy, title='Supreme North Face Backpack By Any Means necessary', description="""This is the most ideal backpack, i want it, but will definetly not pay full price. will happily swap discounts if anyone likes John Smedley""", size="""Size: US 7 / EU 40""", designers=[Supreme], categories=[Accessories], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/XiCwwe5T4mhmvwhY87nA', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/6kfLBpwVRwyiB2M6d3M7', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:2200,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/cTP0KqBTRkqzQWTrbMVa')

    postthirty = ItemPost(creator=Marian, title='Gucci Slides', description="""Going on holiday soon and will need these, preferably 30%+ discount will be prefered. I can offer discount in return""", size="""Size: US 10.5 / EU 43-44""", designers=[Gucci], categories=[Shoes], image1='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/LJ4oqWeKTgmvc2KuW8Py', image2='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/ZP5X9TLqS02nic3rRB92', image3='https://process.fs.grailed.com/AJdAgnqCST4iPtnUxiGtTz/cache=expiry:max/rotate=deg:exif/resize=height:1400,fit:scale/output=format:webp,quality:90/compress/https://cdn.fs.grailed.com/api/file/Wzg7ltxpQPaRfpNVYUcm')





    comment1 = Comment(content='Hi, if you\'re interested, I can get this jacket for you with a 30% discount, I will follow you and let you know if i want anything else in the future', itemPost=postone)

    comment2 = Comment(content='I can get this jacket for 40% however, I see you can get discount at louis vuitton, ill be happy to swap if the discount is right', itemPost=postone)

    comment3 = Comment(content='This is a lovely beanie. ill have to take a cut but i can get it for you for £39,let me know if you\'re interested', itemPost=posttwo)

    comment4 = Comment(content='I want this too, if you can help me out then please follow or messsage me so we can discuss pricing etc', itemPost=postthree)


    db.session.add(Saint_Laurent)
    db.session.add(Gucci)
    db.session.add(Moncler)
    db.session.add(Common_Projects)
    db.session.add(Comme_De_Garcons)
    db.session.add(Acne_Studios)
    db.session.add(Alexaner_Wang)
    db.session.add(Adidas)
    db.session.add(Burberry)
    db.session.add(Prada)
    db.session.add(Trickers)
    db.session.add(Supreme)
    db.session.add(Maison_Margiela)
    db.session.add(Off_White)
    db.session.add(Nike)
    db.session.add(Palace)
    db.session.add(Issey_Miyake)
    db.session.add(Rick_Owens)
    db.session.add(Clothing)
    db.session.add(Shoes)
    db.session.add(Accessories)
    db.session.add(postone)
    db.session.add(posttwo)
    db.session.add(postthree)
    db.session.add(postfour)
    db.session.add(postfive)
    db.session.add(postsix)
    db.session.add(postseven)
    db.session.add(posteight)
    db.session.add(postnine)
    db.session.add(postten)
    db.session.add(posteleven)
    db.session.add(posttwelve)
    db.session.add(postthirteen)
    db.session.add(postfourteen)
    db.session.add(postfifteen)
    db.session.add(postsixteen)
    db.session.add(postseventeen)
    db.session.add(posteighteen)
    db.session.add(postnineteen)
    db.session.add(posttwenty)
    db.session.add(posttwentyone)
    db.session.add(posttwentytwo)
    db.session.add(posttwentythree)
    db.session.add(posttwentyfive)
    db.session.add(posttwentysix)
    db.session.add(posttwentyseven)
    db.session.add(posttwentyeight)
    db.session.add(posttwentynine)
    db.session.add(postthirty)
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(Tommy)
    db.session.add(Michael)
    db.session.add(Marian)
    db.session.add(Joe)
    db.session.add(Marilyn)


    db.session.commit()
