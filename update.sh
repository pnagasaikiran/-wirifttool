echo "███████╗██╗  ██╗███╗   ██╗███████╗██╗   ██╗    ";
echo "╚══███╔╝██║  ██║████╗  ██║╚══███╔╝██║   ██║    ";
echo "  ███╔╝ ███████║██╔██╗ ██║  ███╔╝ ██║   ██║    ";
echo " ███╔╝  ╚════██║██║╚██╗██║ ███╔╝  ██║   ██║    ";
echo "███████╗     ██║██║ ╚████║███████╗╚██████╔╝    ";
echo "╚══════╝     ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝     ";
echo "                                               ";

clear

sudo chmod +x /etc/

clear

sudo chmod +x /usr/share/doc

clear

sudo rm -rf /usr/share/doc/wirifttool/

clear

cd /etc/

clear

sudo rm -rf /etc/wirifttool

clear

mkdir wirifttool

clear

cd wirifttool

clear

git clone https://github.com/wirifit/wirifttool.git

clear

cd wirifttool

clear

sudo chmod +x install.sh

clear

./install.sh

clear
