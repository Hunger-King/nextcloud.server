import os
import polib
import json


def main():
    for type_name in getTypes():
        po_file_path=f"translationfiles/zh_TW/{type_name}.po"

        translations = readJson(jsonPath(type_name))

        zh_po = polib.pofile(po_file_path)
        for entry in zh_po:
            translation_key = entry.msgid
            if entry.msgid_plural:
                translation_key = '_' + entry.msgid + '_::_' + entry.msgid_plural + '_'

            # 從 JSON 獲取翻譯
            translation = translations['translations'].get(translation_key, None)

            # 檢查翻譯是否存在
            if translation is not None:
                if isinstance(translation, list):
                    entry.msgstr = translation[0]
                    entry.msgstr_plural[0] = translation[0]
                    entry.msgstr_plural[1] = translation[0] if len(translation) == 1 else translation[1]
                # 處理單數形式
                else:
                    entry.msgstr = translation

        zh_po.save(po_file_path)

def getTypes():
    return [
        "admin_audit",
        "cloud_federation_api",
        "comments",
        "contactsinteraction",
        "core",
        "dashboard",
        "dav",
        "encryption",
        "federatedfilesharing",
        "federation",
        "files",
        "files_external",
        "files_reminders",
        "files_sharing",
        "files_trashbin",
        "files_versions",
        "lib",
        "lookup_server_connector",
        "oauth2",
        "provisioning_api",
        "settings",
        "sharebymail",
        "systemtags",
        "theming",
        "twofactor_backupcodes",
        "updatenotification",
        "user_ldap",
        "user_status",
        "weather_status",
        "workflowengine",
    ]

def jsonPath(type_name):
    if type_name == "core" or type_name == "lib":
        return f"{type_name}/l10n/zh_TW.json"
    else:
        return f"apps/{type_name}/l10n/zh_TW.json"


def readJson(file_path):
    with open(file_path, 'r') as file:
        # 解析 JSON 數據
        data = json.load(file)
    return data



if __name__ == '__main__':
    main()
