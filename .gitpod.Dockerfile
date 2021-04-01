FROM baneeishaque/gitpod-workspace-full-vnc-1366x768-tint2-pcmanfm-zsh-anaconda3-2020-11

RUN cd $HOME \
 && wget "https://raw.githubusercontent.com/Baneeishaque/edge-connect/master/environment.yml" \
 && conda env create -f environment.yml \
 && rm environment.yml

RUN pyenv global anaconda3-2020.11/envs/edge-connect
RUN echo "conda activate edge-connect" >> ~/.bashrc
RUN echo "conda activate edge-connect" >> ~/.zshrc
