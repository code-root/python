import pandas as pd

# Data
data = {
    "full_name": [
        "Omar Ameer Mohamed Ameen", "محمد مصطفى أحمد الششتاوي", "Mohamed Elshamy",
        "Ibrahim Muhammed Ismail", "Ebrahim mohamed elhariry", "Mohammed mostafa Al-amrousi",
        "احمد السعيد فتوح عبدربه", "Shahd baher galal ammar", "Hanin Ashraf Abdullah",
        "Shady Abdallah", "sara yasser mahmoud abdo", "Tasneem Atif Soliman Omar",
        "Mohamed Ahmed Magoor", "Shehab Fathy Mohamed ElMorshady", "aliMohamedShiblAboAbdeh",
        "Ziad Amer", "Mohamed Mohsen Eldeeb", "Salah Ahmed Shaalaan", "Nrmeen Mohamed Sadek Elaraby",
        "Mohamed Elsawy", "Ahmed Eltahawy Abdallah", "Hamza Mosaad Mohamed Apdelfatah Mohamed",
        "Mohamed Solaiman Mohamed Abo-Zaied", "Omar Ameer Mohamed Ameen", "Ziad Wael Hafez",
        "Menna Soliman Ali Eldakrory", "Amina AbdelAzeez SayedAhmed Marey", "Mahmoud Baioumy",
        "Diaa Mohamed Elsayed Eltaiby", "Abdelrhman Mahmoud Elbahnsawy", "Nouran kadri Aboyousef",
        "مي السيد عبدالوارث", "Alaa Fathalla", "Abdelrahman Elsayed Eldabsha"
    ],
    "phone_number": [
        "01554111002", "01025263865", "01210059818", "01061769047", "01009518390",
        "01005635026", "01125178289", "01098109707", "01112086551", "01030905121",
        "01032328988", "01018435328", "01092783842", "01212163460", "01143584870",
        "01093694586", "01065408426", "01064928120", "01273362092", "01224961715",
        "01022619838", "01275869193", "01014250577", "01554111002", "01123399112",
        "01157378621", "01554399008", "01032005091", "01206215266", "01286644294",
        "01069506582", "01276936228", "01064746262", "01027093601"
    ],
    "city_of_residence": [
        "Tanta", "Tanta", "Samannoud - Gharbia", "Gharbia", "Tanta", "Tanta", "Tanta",
        "Tanta", "Tanta", "Tanta", "Tanta", "Tanta", "Tanta", "Tanta", "Tanta", "Tanta",
        "Tanta", "Tanta", "Tanta", "Tanta", "I am from Cairo and I don't mind living in Tanta",
        "Tanta", "Kafr Elzayat City- Gharbia", "Tanta", "Tanta", "Tanta", "Tanta", "Tanta",
        "Tanta", "Tanta", "tanta", "Tanta", "Tanta", "Tanta"
    ],
    "expected_salary": [
        "10000", "9000", "7000", "8000", "8000", "9000", "6500", "7000", "5000", "10000",
        "9000", "8000", "8000", "7000", "5000", "8000", "8000", "6000", "10000", "10000",
        "12000", "8000", "10000", "10000", "10000", "10000", "10000", "8000", "10000",
        "9000", "9000", "6000", "7000", "10000"
    ],
    "linkedin_profile_url": [
        "https://www.linkedin.com/in/omar-ameer-126b41231/", "At cv", "https://www.linkedin.com/in/mohamed-elshamy15",
        "www.linkedin.com/in/ebrahim-esmail", "https://www.linkedin.com/in/ebrahim-elhariry-279455227/",
        "https://www.linkedin.com/in/mohammed-al-amrousi-bookly_app/", "https://www.linkedin.com/in/ahmed-abdrabou-815419201/",
        "https://www.linkedin.com/in/shahd-baher-55774b23b/", "https://www.linkedin.com/in/hanin-abdullah-0245781b6/",
        "https://www.linkedin.com/in/shadyabdallah98/", "https://www.linkedin.com/in/sarah-yasser-05339522b/",
        "https://www.linkedin.com/in/tasneem3atif/", None, None,
        "https://www.linkedin.com/in/ali-shibl-587261225/", "https://www.linkedin.com/in/ziad-amer-278394252/",
        "https://www.linkedin.com/in/mohamed-mohsen-116526261/", "https://www.linkedin.com/in/salah-shaalaan/",
        "www.linkedin.com/in/nrmeen-sadek", "https://www.linkedin.com/in/elsawy2002/",
        "https://www.linkedin.com/in/ahmed-eltahawy-78147725b/", "https://www.linkedin.com/in/hamza-mosaad-5a1a5b244/",
        "www.linkedin.com/in/mohamed-solaiman-a2b9921b4", "https://www.linkedin.com/in/omar-ameer-126b41231/",
        "http://linkedin.com/in/ziad-hafez11", "https://www.linkedin.com/in/menna-soliman-7a61b81b6/",
        "https://www.linkedin.com/in/amina-abdelazeez-b24283274/", "www.linkedin.com/in/mahmoud-baioumy-05b36627a",
        "https://www.linkedin.com/in/diaa-el-taiby-6486a2229/", "https://www.linkedin.com/in/abdelrhman-elbahnsawy-2509a0232/",
        None, "https://www.linkedin.com/in/mai-elsaed-92a2932a/", "linkedin.com/in/alaa-fathalla-12408423b",
        "https://www.linkedin.com/in/abdelrahman-eldabsha/"
    ],
    "github_profile_url": [
        "https://github.com/OmarAmeer96", "At cv", "https://github.com/mohamedelshamy6",
        "https://github.com/ebrahimesmail11", "https://github.com/Ebrahimelhariryy",
        "https://github.com/Malamrousi/bookly_app", "https://github.com/AhmedAbdrabou22",
        "https://github.com/Shahdbaherr", "https://github.com/Hanine-abdullah",
        "https://github.com/ShadyAbdallah1998", "https://github.com/sarahyabdou",
        "https://github.com/Tasneem-3atif", "https://github.com/mohamedmagoor",
        "https://github.com/shehabfathy", "https://github.com/Ali-Shibl",
        "https://github.com/ziad-amer-1", "github.com/MohamedMohsen72",
        "https://github.com/SalahShaalaan?tab=repositories", "https://github.com/nrmeenmohamed",
        "https://github.com/Elsawy200", "https://github.com/ahmed-eltahawy",
        "https://github.com/Hamza2542002", "https://github.com/mohamedSolaiman11",
        "https://github.com/OmarAmeer96", "https://github.com/Hafez300",
        "https://github.com/MennaSoliman2", "https://github.com/AminaAbdElAzeez",
        "https://github.com/MahmoudBaioumy", "https://github.com/diaa852000",
        "https://github.com/Abdelrhman066", "https://github.com/engnouran12",
        "https://github.com/maiElsaed", "github.com/Alaafathalla",
        "https://github.com/AbdelrahmanEldabsha"
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving to Excel
file_path = "user_data.xlsx"
df.to_excel(file_path, index=False)

file_path
