# from urllib import response
# import pytest
# from fastapi.testclient import TestClient
# import sys
# import os


# current = os.path.dirname(os.path.realpath(__file__))
# parent = os.path.dirname(current)
# sys.path.append(parent)

# from main import app

# client = TestClient(app)


# # def test_youtube():
# #     """This test will check if the youtube downloader is working"""
# #     response = client.get(
# #         "/api/yt?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Duc6vV8o_aAU")
# #     assert response.json()['status'] == "ok"


# def test_tiktok_downloader():
#     """This test will check if the tiktok downloader is working"""
#     response = client.get(
#         "/api/tk?url=https://www.tiktok.com/@majhc/video/7049993308386495745")
#     assert response.json()["success"]


# def test_twitter_downloader():
#     """This test will check if the twitter downloader is working"""
#     response = client.get(
#         "/api/twitter?url=https%3A%2F%2Ftwitter.com%2FOmanTVGeneral%2Fstatus%2F1478376146907668483%3Fs%3D20")
#     assert response.json()['status'] == "ok"


# def test_twitter_downloader_2():
#     """This test will check if the twitter downloader is working"""
#     response = client.get(
#         "/api/tw?url=https://twitter.com/OmanTVGeneral/status/1478376146907668483?s=20")
#     assert "title" in response.text


# def test_btc():
#     """This test will check if the btc is working"""
#     response = client.get("/api/BTC")
#     assert response.status_code == 200


# def test_eth():
#     """This test will check if the eth is working"""
#     response = client.get("/api/ETH")
#     assert response.status_code == 200


# def test_ip():
#     """This test will check if the ip is working"""
#     response = client.get("/api/ip")
#     assert response.status_code == 200


# def test_fake_add():
#     """This test will check if the fake add is working"""
#     response = client.get("/api/fake-address")
#     assert response.status_code == 200




# def test_caller_id():
#     """This test will check if the caller id is working"""
#     response = client.get("/api/caller-id?country_code=US&number=123456789")
#     assert response.json()['status'] == "success"


# def test_google_mail_checker():
#     """This test will check if the google mail checker is working"""
#     response = client.get(
#         "/api/email/checker/google?email=oman4omani%40gmail.com")
#     assert response.json()['status'] == "success"


# def test_microsoft_mail_checker():
#     """This test will check if the gmail mail checker is working"""
#     response = client.get(
#         "/api/email/checker/microsoft?email=oman4omani%40outlook.com")
#     assert response.json()['status'] == "success"


# def test_get_last_video_tiktok():
#     """This test will check if the last video tiktok is working"""
#     response = client.get("/api/tk/getlastvideoid?username=majhcc")
#     assert response.json()['status'] == "success"


# # def test_get_last_video_youtube_by_id():
# #     """This test will check if the last video youtube is working"""
# #     response = client.get(
# #         "/api/get_last_videoid_youtube?channel_id=UCnddj1RPMErfmyUMGULawZQ")
# #     assert response.json()['status'] == "success"


# # def test_get_last_video_youtube_by_username():
# #     """This test will check if the last video youtube is working"""
# #     response = client.get(
# #         "/api/get_last_videoid_youtube_by_username?username=majhcc")
# #     assert response.json()['status'] == "success"


# def test_get_user_info_tiktok():
#     """This test will check if the user info tiktok is working"""
#     response = client.get("/api/tk/get_user_info?username=majhc")
#     assert response.json()['status'] == "success"


# def test_check_user_tiktok():
#     """This test will check if the user info tiktok is working"""
#     response = client.get("/api/tk/check_user_exist?username=majhc")
#     assert response.json()['status'] == "success"


# def test_get_list_of_video_tiktok():
#     """This test will check if the user info tiktok is working"""
#     response = client.get(
#         "/api/tk/full_list_videos_id_by_username?username=majhc")
#     assert response.status_code == 200


# # def test_mailru_checker():
# #     """This test will check if the mailru checker is working"""
# #     response = client.get("/api/email/checker/mailru?email=oman4omani@mail.ru")
# #     assert response.json()['status'] == "success"


# def test_names_meaning():
#     """this tes wihll check if the name meaning is working"""
#     response = client.get("/api/meaning/ar?name=محمد")
#     assert response.json()['status'] == True
