Summary:	Desktop Background Images from www.kde-look.org
Summary(pl):	Obrazki na t³o pulpitu z www.kde-look.org
Name:		desktop-wallpapers-kdelook
Version:	00
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://arg0.net/users/vgough/images/2333-valley.png
# Source0-md5:	476a843ab52775eb412089f277c0083b
#Type:  KDE Wallpaper 1600x1200
Source1:	http://www.kde-look.org/content/files/24919-kitov_py001.jpg
# Source1-md5:	954b159341286dda358201ae782bcaca
#Type:  KDE Wallpaper 1600x1200
Source2:	http://www.kde-look.org/content/files/25016-3D57_3DI5G73.jpg
# Source2-md5:	bd756901ad5a1ff29095156e84b6e523
#Type:  KDE Wallpaper 1280x1024
Source3:	http://www.kde-look.org/content/files/23484-durrutilinux.png
# Source3-md5:	69f5f4e3b84aebfb752c919d2cdbc92e
#Type:  KDE Wallpaper 1024x768
Source4:	http://www.kde-look.org/content/files/17449-Bubbles.jpg
# Source4-md5:	392f372276be7f31c2ed04e9e10eeda6
#Type:  KDE Wallpaper 1600x1200
Source5:	http://www.kde-look.org/content/files/19342-KDE34-SVG.tar.gz
# Source5-md5:	7ca5b783f6eb8dd859d5232c986db571
#Type:	KDE SVG wallpaper (kde 3.4)
Source6:	http://www.kde-look.org/content/files/19501-kostka.jpg
# Source6-md5:	363cf11f62d6e8efc04236540823b8a5
#Type:	Type:  KDE Wallpaper 1024x768
Source7:	http://aliendonald.w.interia.pl/cubebluee.png
# Source7-md5:	f2c71e02ceb0b10694f3f5a34882fde5
#Type:  Type:  KDE Wallpaper 1024x768
Source8:	http://www.kde-look.org/content/files/20209-altabadia_snow_1600.jpg
# Source8-md5:	f300e583a45aed051cd62e82edb67083
#Type:  KDE Wallpaper 1600x1200
Source9:	http://www.kde-look.org/content/files/20263-kde3.4-v02-1600.png
# Source9-md5:	8f015fc19e46a44da1bc4a635bbdd4e7
#Type:  KDE Wallpaper 1600x1200
Source10:	http://www.kde-look.org/content/files/23814-mars_sunset-1.jpg
# Source10-md5:	9e82f3d4799d1f32558458f65008a940
#Type:  KDE Wallpaper 1024x768
Source11:	http://www.kde-look.org/content/pre2/23814-2.jpg
# Source11-md5:	45d39f57e17d2359a365165d18be9d7e
#Type:  KDE Wallpaper 1024x768
Source12:	http://www.kde-look.org/content/files/20979-altabadia_summer_1200.jpg
# Source12-md5:	1c6b047dfdfcf8627eb79a9e99f9edfd
#Type:  KDE Wallpaper 1600x1200
Source13:	http://www.kde-look.org/content/files/23096-Haallborgsaan.jpg
# Source13-md5:	e93507e859d44537d93decec2b1f0236
#Type:  KDE Wallpaper 1600x1200

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
Desktop Background Images from www.kde-look.org.

%description -l pl
Obrazki na t³o pulpitu z www.kde-look.org. 

%prep
%setup -q -c %{name}-%{version} -T -D

cp -f %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} .
cp -f %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
install *.{jpg,png} $RPM_BUILD_ROOT%{_datadir}/wallpapers

cd $RPM_BUILD_ROOT%{_datadir}/wallpapers
tar xzf %{SOURCE5}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers
