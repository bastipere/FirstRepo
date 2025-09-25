import imageio.v3 as iio

filenames = ['a1.png', 
             'a2.png', 
             'a3.png',
             'a4.png',
             'a5.png',
             'b1.png',
             'b2.png',
             'b3.png',
             'c1.png',
             'c2.png',
             'c3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('poke.gif', images, duration = 500, loop = 0)


