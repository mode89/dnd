map \b :!clear && docker build --tag dnd $PWD/docker
map \r :!clear && docker run -it --rm --publish 5000:5000 --volume $PWD:/srv/dnd dnd python3 /srv/dnd
