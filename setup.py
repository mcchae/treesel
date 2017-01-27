# !/usr/bin/python
# coding=utf-8

################################################################################
from setuptools import setup  # , find_packages
import treesel

setup_requires = []

# 패키지에 필요한 사전 설치 패키지 입니다.
install_requires = [
]

dependency_links = [
]

setup(
    # 패키지 이름
    name='treesel',
    # 패키지 버전 - 버전이 바뀌어야 pypi에 업로드 됩니다. 버전이 바뀌지 않으면 바뀐사항이 업로드 되지 않습니다.
    version=treesel.__version__,
    # 패키지 관련 홈페이지 주소
    url='https://github.com/mcchae/treesel',
    # 패키지의 라이센스
    license='MIT License',
    # 패키지에 대한 간략한 설명
    description='Small python program select tree and change it '
                'using curses standard library ',
    # 패키지에 대한 상세 설명
    #long_description=readme,
    # 패키지 제작자 정보
    author='mcchae',
    author_email='mcchae@gmail.com',
    # 업로드에 포함할 패키지들
    # packages=["treesel"],
    py_modules = ['treesel'],
    # include_package_data=True,
    # 위에 작성한 사전 설치 패키지
    # install_requires=install_requires,

    setup_requires=setup_requires,
    dependency_links=dependency_links,
    # 자신의 패키지에 달 키워드 - 본인이 원하는 키워드로 자유롭게 달면 됩니다.
    keywords=['tree', 'curses', 'utility', 'change', 'directory'],
    # 패키지 분류 - 이건 pypi에 있는 분류에 맞춰 작성해야합니다. 아무것이나 넣었다간 빌드실패합니다.
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'treesel=treesel:main',
        ],
    },
)
