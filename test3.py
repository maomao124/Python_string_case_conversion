"""
 * Project name(项目名称)：Python字符串大小写转换
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:38
 * Version(版本): 1.0
 * Description(描述)： Python upper()方法
upper() 的功能和 lower() 方法恰好相反，它用于将字符串中的所有小写字母转换为大写字母，
和以上两种方法的返回方式相同，即如果转换成功，则返回新字符串；反之，则返回原字符串。
 """

if __name__ == '__main__':
    print("hello".upper())
    print("1hello".upper())
    print("2335252hello".upper())
    print("你好hello".upper())
    str1 = "converts the first letter of each word in a string to uppercase"
    print(str1.upper())
    str1 = "convertsthefirstletterofeachwordinastringtouppercase"
    print(str1.upper())
    print("HELLOhe".upper())

    input()
