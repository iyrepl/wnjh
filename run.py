version: 2.1

jobs:
  extend:
    docker:
      - image: cimg/python:3.11.1
    resource_class: small
    steps:
      - checkout
      - run: 
          name: Upgrade pip
          command: /home/circleci/.pyenv/versions/3.11.1/bin/python3.11 -m pip install --upgrade pip
      - run: 
          name: Insall Dependices
          command: pip3 install requests
      - run: 
          name: Extend
          command: python3 run.py
workflows:
  extend:
    jobs:
      - extend
