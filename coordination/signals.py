
MANAGER_GROUP_NAME = 'Manager'
ADMINISTRATOR_GROUP_NAME = 'Administrator'
APARTMENT_GROUP_NAME = 'Mieszkania'
TRANSPORT_GROUP_NAME = 'Transport'
COLLECTION_GROUP_NAME = 'Collection'
SPONSOR_GROUP_NAME = 'Sponsor'
MEDIA_GROUP_NAME = 'Media'
SUBGROUP_GROUP_NAME = 'Subgroup'
ATTACHMENT_GROUP_NAME = 'Attachment'

APARTMENT_GROUP_TYPE = 1001
TRANSPORT_GROUP_TYPE = 1002
COLLECTION_GROUP_TYPE = 1003
SPONSOR_GROUP_TYPE = 1004
MEDIA_GROUP_TYPE = 1005
ONEOFFACCTION_GROUP_TYPE = 1006
APPLICATION_GROUP_TYPE = 1007
TASK_GROUP_TYPE = 1008

SUBGROUP_GROUP_TYPE = 2001
STATUS_GROUP_TYPE = 2002
ATTACHMENT_GROUP_TYPE= 2003
ADMINISTRATOR_GROUP_TYPE= 2004
MANAGER_GROUP_TYPE= 2005
VOIVODESHIP_GROUP_TYPE = 2006
REGION_GROUP_TYPE = 2007

REGION_POLAND_NAME = 'Polska'
REGION_POLAND_CODE = 48
REGION_UKRAINE_NAME = 'Ukraina'
REGION_UKRAINE_CODE = 380

VOIVODESHIPS_POLAND_DOLNOSLONSKIE_NAME = 'dolnośląskie'
VOIVODESHIPS_POLAND_KUJPOM_NAME = 'kujawsko-pomorskie'
VOIVODESHIPS_POLAND_LUBEL_NAME = 'lubelskie'
VOIVODESHIPS_POLAND_LUBUS_NAME = 'lubuskie'
VOIVODESHIPS_POLAND_LODZ_NAME = 'łódzkie'
VOIVODESHIPS_POLAND_MOLOPOL_NAME = 'małopolskie'
VOIVODESHIPS_POLAND_MAZOW_NAME = 'mazowieckie'
VOIVODESHIPS_POLAND_OPOL_NAME = 'opolskie'
VOIVODESHIPS_POLAND_PODKAR_NAME = 'podkarpackie'
VOIVODESHIPS_POLAND_PODLAS_NAME = 'podlaskie'
VOIVODESHIPS_POLAND_POMOR_NAME = 'pomorskie'
VOIVODESHIPS_POLAND_SLASK_NAME = 'śląskie'
VOIVODESHIPS_POLAND_SWIETO_NAME = 'świętokrzyskie'
VOIVODESHIPS_POLAND_WARMAZ_NAME = 'warmińsko-mazurskie'
VOIVODESHIPS_POLAND_WIELKOPOL_NAME = 'wielkopolskie'
VOIVODESHIPS_POLAND_ZACHPOM_NAME = 'zachodniopomorskie'

VOIVODESHIPS_UKRAINE_CHERKASY_NAME = 'Cherkasy Oblast'
VOIVODESHIPS_UKRAINE_CHERNIHIV_NAME = 'Chernihiv Oblast'
VOIVODESHIPS_UKRAINE_CHERNIVTSI_NAME = 'Chernivtsi Oblast'
VOIVODESHIPS_UKRAINE_DNIPRO_NAME = 'Dnipropetrovsk Oblast'
VOIVODESHIPS_UKRAINE_DONETSK_NAME = 'Donetsk Oblast'
VOIVODESHIPS_UKRAINE_IVANO_NAME = 'Ivano-Frankivsk Oblast'
VOIVODESHIPS_UKRAINE_KHARKIV_NAME = 'Kharkiv Oblast'
VOIVODESHIPS_UKRAINE_KHERSON_NAME = 'Kherson Oblast'
VOIVODESHIPS_UKRAINE_KHMELNYT_NAME = 'Khmelnytskyi Oblast'
VOIVODESHIPS_UKRAINE_KYIV_NAME = 'Kyiv Oblast'
VOIVODESHIPS_UKRAINE_KIROV_NAME = 'Kirovohrad Oblast'
VOIVODESHIPS_UKRAINE_LUHANSK_NAME = 'Luhansk Oblast'
VOIVODESHIPS_UKRAINE_LVIV_NAME = 'Lviv Oblast'
VOIVODESHIPS_UKRAINE_MYKOLA_NAME = 'Mykolaiv Oblast'
VOIVODESHIPS_UKRAINE_ODESSA_NAME = 'Odessa Oblast'
VOIVODESHIPS_UKRAINE_POLT_NAME = 'Poltava Oblast'
VOIVODESHIPS_UKRAINE_RIVNE_NAME = 'Rivne Oblast'
VOIVODESHIPS_UKRAINE_SUMY_NAME = 'Sumy Oblast'
VOIVODESHIPS_UKRAINE_TERNOP_NAME = 'Ternopil Oblast'
VOIVODESHIPS_UKRAINE_VINNYT_NAME = 'Vinnytsia Oblast'
VOIVODESHIPS_UKRAINE_VOLYN_NAME = 'Volyn Oblast(Lutsk)'
VOIVODESHIPS_UKRAINE_ZAKARP_NAME = 'Zakarpattia Oblast(Uzhorod)'
VOIVODESHIPS_UKRAINE_ZAPOROZ_NAME = 'Zaporizhzhia Oblast'
VOIVODESHIPS_UKRAINE_ZYTOM_NAME = 'Zhytomyr Oblast'
VOIVODESHIPS_UKRAINE_KRYM_NAME = 'Autonomous Republic of Crimea'

REGION_POLAND_ID = 1
REGION_UKRAINE_ID = 2

STATUS_NEW = 'Nowy'
STATUS_INPROGRESS = 'W Realizacji'
STATUS_ARCHIVE = 'Archiwum'

def generate_groups(apps, **kwargs):
    Group = apps.get_model('coordination', 'Department')
    Group.objects.get_or_create(name=ADMINISTRATOR_GROUP_NAME, object_type=ADMINISTRATOR_GROUP_TYPE)
    Group.objects.get_or_create(name=MANAGER_GROUP_NAME, object_type=MANAGER_GROUP_TYPE)
    Group.objects.get_or_create(name=APARTMENT_GROUP_NAME, object_type=APARTMENT_GROUP_TYPE)
    Group.objects.get_or_create(name=TRANSPORT_GROUP_NAME, object_type=TRANSPORT_GROUP_TYPE)
    Group.objects.get_or_create(name=COLLECTION_GROUP_NAME, object_type=COLLECTION_GROUP_TYPE)
    Group.objects.get_or_create(name=SPONSOR_GROUP_NAME, object_type=SPONSOR_GROUP_TYPE)
    Group.objects.get_or_create(name=MEDIA_GROUP_NAME, object_type=MEDIA_GROUP_TYPE)


def generate_regions(apps, **kwargs):
    Region = apps.get_model('coordination', 'Region')
    Region.objects.get_or_create(name=REGION_POLAND_NAME, code=REGION_POLAND_CODE, object_type=REGION_GROUP_TYPE)
    Region.objects.get_or_create(name=REGION_UKRAINE_NAME, code=REGION_UKRAINE_CODE, object_type=REGION_GROUP_TYPE)

def generate_aplication_status(apps, **kwargs):
    AplicationStatus = apps.get_model('coordination', 'Status')
    AplicationStatus.objects.get_or_create(name=STATUS_NEW, object_type=STATUS_GROUP_TYPE)
    AplicationStatus.objects.get_or_create(name=STATUS_INPROGRESS, object_type=STATUS_GROUP_TYPE)
    AplicationStatus.objects.get_or_create(name=STATUS_ARCHIVE, object_type=STATUS_GROUP_TYPE)

def generate_voivodeships(apps, **kwargs):
    Voivodeship = apps.get_model('coordination', 'Voivodeship')
    Region = apps.get_model('coordination', 'Region')

    poland = Region.objects.get(pk=REGION_POLAND_ID)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_DOLNOSLONSKIE_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_KUJPOM_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_LUBEL_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_LUBUS_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_LODZ_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_MOLOPOL_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_MAZOW_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_OPOL_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_PODKAR_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_PODLAS_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_POMOR_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_SLASK_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_SWIETO_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_WARMAZ_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_WIELKOPOL_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_POLAND_ZACHPOM_NAME, region=poland, object_type=VOIVODESHIP_GROUP_TYPE)

    ukraine = Region.objects.get(pk=REGION_UKRAINE_ID)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_CHERKASY_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_CHERNIHIV_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_CHERNIVTSI_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_DNIPRO_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_DONETSK_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_IVANO_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KHARKIV_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KHERSON_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KHMELNYT_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KYIV_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KIROV_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_LUHANSK_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_LVIV_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_MYKOLA_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_ODESSA_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_POLT_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_RIVNE_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_SUMY_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_TERNOP_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_VINNYT_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_VOLYN_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_ZAKARP_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_ZAPOROZ_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_ZYTOM_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)
    Voivodeship.objects.get_or_create(name=VOIVODESHIPS_UKRAINE_KRYM_NAME, region=ukraine, object_type=VOIVODESHIP_GROUP_TYPE)

