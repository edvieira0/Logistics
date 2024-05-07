from source.browser.browser import Browser
from scts import user_logistic, password_logistic
from source.package import package
from scts import management_url

packages_ids = [
    43332964864,
    43338888166,
    43339921850,
    43333804110,
    43340133684,
    43335804296,
    43346570094,
    43338049059,
    43345158175,
    43345083099,
    43346123461,
    43348423224,
    43351657012,
    43335559702
]


instance_teste = package.Package(Browser('chrome'))
instance_teste.login(user_logistic, password_logistic)
for i in packages_ids:
    instance_teste.extract_infos(f'{management_url}{i}')