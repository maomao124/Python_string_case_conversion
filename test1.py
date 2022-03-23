"""
 * Project name(项目名称)：Python字符串大小写转换
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:31
 * Version(版本): 1.0
 * Description(描述)： Python title()方法
title() 方法用于将字符串中每个单词的首字母转为大写，其他字母全部转为小写，转换完成后，
此方法会返回转换得到的字符串。如果字符串中没有需要被转换的字符，此方法会将字符串原封不动地返回。
 """

if __name__ == '__main__':
    print("hello".title())
    print("1hello".title())
    print("2335252hello".title())
    print("你好hello".title())
    str1 = "converts the first letter of each word in a string to uppercase"
    print(str1.title())
    str1 = "convertsthefirstletterofeachwordinastringtouppercase"
    print(str1.title())

    input()
