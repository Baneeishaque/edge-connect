FROM baneeishaque/gitpod-full-tint2-pcmanfm-zsh-as-gh-chrome-idea-pycharm-anaconda3-2020-11-as-canary-1366x625

RUN cd $HOME \
 && wget "https://raw.githubusercontent.com/Baneeishaque/edge-connect/master/environment.yml" \
 && conda env create -f environment.yml \
 && rm environment.yml

RUN pyenv global anaconda3-2020.11/envs/edge-connect
RUN echo "conda activate edge-connect" >> ~/.bashrc
RUN echo "conda activate edge-connect" >> ~/.zshrc
