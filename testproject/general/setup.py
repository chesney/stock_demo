'''
Created on 07 Feb 2015

@author: JANDRE-PRETORIUS
'''
import os, sys
base_path = os.path.split(os.path.abspath(globals()['__file__']))[0]
base_path_parts = base_path.split(os.sep)
for index in range(len(base_path_parts), 0, -1):
    search_path = os.sep.join(base_path_parts[0:index])
    if os.access(os.path.join(search_path, 'settings.py'), os.F_OK):
        break

sys.path.insert(0, search_path)
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
import general.models
if __name__ == '__main__':

    names = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia-Herzegovina", "Botswana", "Bouvet Island", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo, Democratic Republic of the (Zaire)", "Congo, Republic of", "Cook Islands", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe (French)", "Guam (USA)", "Guatemala", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast (Cote D`Ivoire)", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique (French)", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia (French)", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "North Korea", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn Island", "Poland", "Polynesia (French)", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saint Helena", "Saint Kitts and Nevis", "Saint Lucia", "Saint Pierre and Miquelon", "Saint Vincent and Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and South Sandwich Islands", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste (East Timor)", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands", "Wallis and Futuna Islands", "Yemen", "Zambia", "Zimbabwe"]
    districts = ["A of Adrion", "Aangelee", "Aangelegen", "Aangelegen", "Aanstoot", "Aanstoot", "Aapieshoek", "Aardappel Kraal", "Aasvogel Krans", "Aasvogel Krans", "Aberdour", "Abergeldie", "Abergeldy", "Aboretum", "Aboyne", "Achleean", "Acme", "Acol", "Acton Homes", "Adams College", "Adams M.S.", "Adams Mission", "Adams Mission Station", "Addington", "Addington", "Adelaide", "Adventure", "Afelele", "Afgesnij", "Agatha", "Ahrens", "Alan Holmes", "Albert", "Albert Falls", "Alcock", "Alcockspruit", "Alderly", "Aldinville", "Aletta", "Alicedale", "Alida", "Alida Mount", "Allan Holm", "Alleen No. 1", "Alleen No. 2", "Alleen Number One", "Alleen Number Two", "Allendale", "Allendale", "Allermans Drift", "Allerton", "Alleta", "Alma", "Almansdrift", "Almansnek", "Aloe Corner", "Aloe Dale", "Aloe Flats", "Aloeboom", "Alston", "Altemooi", "Altenburg", "Alto", "Alton", "Altona", "Altona", "Altoona", "Alva", "Alwyns Poort", "Amalinda Paddavlei", "Amanda", "Amanzana", "Amanzimtoti", "Ambleside", "Ambleton", "American Mission", "Amiel Park", "Amitikulu Station", "Anbrey", "Anerley", "Annandale", "Annexatie", "Annie", "Antiford", "Aomori", "Apologie", "Appelbos", "Appelsbosch", "Appelsbosch", "Aquocane", "Arbor Park", "Arboretum", "Arborfield", "Arborville", "Arcadia", "Arcadia", "Arcadia", "Arcadia", "Ardee", "Ardmore", "Argyle", "Arnolds", "Arrarat", "Arrochar", "Ashley", "Ashley", "Ashley", "Ashton", "Assagay Kraal", "Assina", "Aston Lodge", "Asvogel Krantz", "Asyn Kraal", "Athalie", "Atherstone", "Athlone", "Atholdene", "Aubrey", "Aussicht", "Austerville", "Avocadale", "Avondale", "Avondstond", "Avonduur", "Paapkuilvly", "Paapkuilvly", "Paard Fontein", "Paarde Berg", "Paarde Fontein", "Paarde Fontein", "Paarde Kraal", ]
    for name in names:
        country = general.models.Country.objects.create(name=name, abbreviation=name[:3])

    setup_c = general.models.Country.objects.get(name="South Africa")

    for dist in districts:
        district = general.models.District.objects.create(name=dist, abbreviation=name[:3], country=setup_c)