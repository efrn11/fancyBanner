import sys

from fancyBanner.fancyBannerUni import *


width_range = range(1, 100, 1)

# test run

for width in width_range:
    FancyBannerUni.width = width

    print(OneSec(str(width)))
    print(OneSecMain(str(width)))
    print(OneSecMega(str(width)))

    print(TwoSec())
    print(TwoSecMain())
    print(TwoSecMainHor())
    print(TwoSecMega())

    print(ThreeSec())
    print(ThreeSecMain())
    print(ThreeSecMega())

    print(Ribbon())
    print(SmallRibbon('allala'))

