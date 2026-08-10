"""
    要点:
        1.深浅拷贝分别指copy模块的copy()和deepcopy()函数
        2.深浅拷贝主要针对于可变类型来讲的,深拷贝拷贝所有层(可变),浅拷贝只第一层(可变)
        3.如果是不可变类型,和普通赋值一样
"""
import copy
#普通赋值
def dm01_copy():
    a= 10
    b= a
    print("id(a):",id(a))
    print("id(b):",id(b))
    print("id(10):",id(10))

    #k可变类型
    a=[1,2,3]
    b = [11,22,33]
    c=[a,b]
    d=c
    print("id(c):",id(c))
    print("id(d):",id(d))

#浅拷贝可变类型(列表)
def dm02_copy():
    a = [1,2,3]
    b = [11,22,33]
    c = [6,7,a,b]

    d=copy.copy(c)
    print("id(c):",id(c)) #0x01
    print("id(d):",id(d)) #0x02
    #test02
    print(id(c[2]))
    print(id(a))

    #test03
    a[2]=22
    c[0]=100
    print("c:",c)
    print("d:",d)

#浅拷贝不可变类型(元组)
def dm03_copy():
    a = (1,2,3)
    b = (11,22,33)
    c = (6,7,a,b)

    d=copy.copy(c)
    print("id(c):",id(c))
    print("id(d):",id(d))
    print("id(c)和id(d)值一样,说明c和d指向相同的内存空间")

#深拷贝可变类型
def dm04_copy():
    a = [1,2,3]
    b = [11,22,33]
    c = [6,7,a,b]

    d=copy.deepcopy(c)
    print("id(c):",id(c))
    print("id(d):",id(d))


    a[1] = 100
    b[1] = 800
    print(f"c:{c}")
    print(f"d:{d}")

#深拷贝不可变类型
def dm05_copy():
    a = (1,2,3)
    b = (11,22,33)
    c = (6,7,a,b)

    d=copy.deepcopy(c)
    print("id(c):",id(c))
    print("id(d):",id(d))

if __name__ == "__main__":
    # dm01_copy()
    # dm02_copy()
    # dm03_copy()
    # dm04_copy()
    dm05_copy()