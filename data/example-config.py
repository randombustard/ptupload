config = {
    "DEFAULT": {

        # ------ READ THIS ------
        # Any lines starting with the # symbol are commented and will not be used.
        # If you change any of these options, remove the #
        # -----------------------

        "tmdb_api": "tmdb_api key",
        "imgbb_api": "imgbb api key",
        "ptpimg_api": "ptpimg api key",
        "lensdump_api": "lensdump api key",

        # Order of image hosts, and backup image hosts
        "img_host_1": "imgbb",
        "img_host_2": "ptpimg",
        "img_host_3": "imgbox",
        "img_host_4": "pixhost",
        "img_host_5": "lensdump",


        "screens": "6",
        # Enable lossless PNG Compression (True/False)
        "optimize_images": True,


        # The name of your default torrent client, set in the torrent client sections below
        "default_torrent_client": "Client1",

        # Play the bell sound effect when asking for confirmation
        "sfx_on_prompt": True,

    },

    "TRACKERS": {
        # Which trackers do you want to upload to?
        "default_trackers": "BLU, BHD, AITHER, STC, STT, SN, THR, R4E, HP, ACM, PTP, LCD, LST, PTER, NBL, ANT, MTV",

        "BLU": {
            "useAPI": False,  # Set to True if using BLU
            "api_key": "BLU api key",
            "announce_url": "https://blutopia.cc/announce/customannounceurl",
            # "anon": False
        },
        "BHD": {
            "api_key": "BHD api key",
            "announce_url": "https://beyond-hd.me/announce/customannounceurl",
            "draft_default": "True",
            "anon": True
        },
        "PTP": {
            "useAPI": False,  # Set to True if using PTP
            "add_web_source_to_desc": True,
            "ApiUser": "ptp api user",
            "ApiKey": 'ptp api key',
            "username": "",
            "password": "",
            "announce_url": ""
        },
        "AITHER": {
            "api_key": "AITHER api key",
            "announce_url": "https://aither.cc/announce/customannounceurl",
            # "anon": False
        },
        "HUNO": {
            "api_key": "HUNO api key",
            "announce_url": "https://hawke.uno/announce/customannounceurl",
            "anon": True
        },
        "MTV": {
            'api_key': 'get from security page',
            'username': '<USERNAME>',
            'password': '<PASSWORD>',
            'announce_url': "get from https://www.morethantv.me/upload.php",
            'anon': True,
            # 'otp_uri' : 'OTP URI, read the following for more information https://github.com/google/google-authenticator/wiki/Key-Uri-Format'
        },
        "LT": {
            "api_key": "LT api key",
            "announce_url": "https://lat-team.com/announce/customannounceurl",
            # "anon": False
        },
        "PTER": {
            "passkey": 'passkey',
            "img_rehost": False,
            "username": "",
            "password": "",
            "ptgen_api": "",
            "anon": True,
        },
        "TL": {
            "announce_key": "TL announce key",
        },
        "HDT": {
            "username": "username",
            "password": "password",
            "my_announce_url": "https://hdts-announce.ru/announce.php?pid=<PASS_KEY/PID>",
            # "anon": "False"
            "announce_url": "https://hdts-announce.ru/announce.php",  # DO NOT EDIT THIS LINE
        },
        "OE": {
            "api_key": "OE api key",
            "announce_url": "https://onlyencodes.cc/announce/customannounceurl",
            # "anon": False
        },
        "MANUAL": {
            # Uncomment and replace link with filebrowser (https://github.com/filebrowser/filebrowser) link to the Upload-Assistant directory, this will link to your filebrowser instead of uploading to uguu.se
            # "filebrowser": "https://domain.tld/filebrowser/files/Upload-Assistant/"
        },
    },


    "TORRENT_CLIENTS": {
        # Name your torrent clients here, for example, this example is named "Client1"
        "Client1": {
            "torrent_client": "qbit",
            "qbit_url": "http://127.0.0.1",
            "qbit_port": "8080",
            "qbit_user": "username",
            "qbit_pass": "password",

            # Remote path mapping (docker/etc.) CASE SENSITIVE
            # "local_path": "/LocalPath",
            # "remote_path": "/RemotePath"
        },
        "qbit_sample": {
            "torrent_client": "qbit",
            "enable_search": True,
            "qbit_url": "http://127.0.0.1",
            "qbit_port": "8080",
            "qbit_user": "username",
            "qbit_pass": "password",
            # "torrent_storage_dir": "path/to/BT_backup folder"
            # "qbit_tag": "tag",
            # "qbit_cat": "category"

            # Content Layout for adding .torrents: "Original"(recommended)/"Subfolder"/"NoSubfolder"
            "content_layout": "Original"

            # Enable automatic torrent management if listed path(s) are present in the path
            # If using remote path mapping, use remote path
            # For using multiple paths, use a list ["path1", "path2"]
            # "automatic_management_paths": ""



            # Remote path mapping (docker/etc.) CASE SENSITIVE
            # "local_path": "E:\\downloads\\tv",
            # "remote_path": "/remote/downloads/tv"

            # Set to False to skip verify certificate for HTTPS connections; for instance, if the connection is using a self-signed certificate.
            # "VERIFY_WEBUI_CERTIFICATE": True
        },

        "rtorrent_sample": {
            "torrent_client": "rtorrent",
            "rtorrent_url": "https://user:password@server.host.tld:443/username/rutorrent/plugins/httprpc/action.php",
            # "torrent_storage_dir": "path/to/session folder",
            # "rtorrent_label": "Add this label to all uploads"

            # Remote path mapping (docker/etc.) CASE SENSITIVE
            # "local_path": "/LocalPath",
            # "remote_path": "/RemotePath"

        },
        "deluge_sample": {
            "torrent_client": "deluge",
            "deluge_url": "localhost",
            "deluge_port": "8080",
            "deluge_user": "username",
            "deluge_pass": "password",
            # "torrent_storage_dir": "path/to/session folder",

            # Remote path mapping (docker/etc.) CASE SENSITIVE
            # "local_path": "/LocalPath",
            # "remote_path": "/RemotePath"
        },
        "watch_sample": {
            "torrent_client": "watch",
            "watch_folder": "/Path/To/Watch/Folder"
        },

    },
}
