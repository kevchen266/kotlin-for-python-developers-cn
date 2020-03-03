# vim:fileencoding=utf-8

from sys import stdin
import re

seen_preamble = False
section_slugs = set()
current_section = None
current_section_slug = None
sections = []
link_regex = re.compile(r"\]\(#([^)]+)\)")
subsection_slugs = {}
copyright_notice = (
    u"*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；"
    u"其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，"
    u"授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）]"
    u"(https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。"
    u"请注意，这并不是可汗学院官方产品的一部分。"
    u"中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*")
copyright_notice_separator = "\n\n---\n\n"

def substitute_link(match):
    link = match.group(1)
    if link in section_slugs:
        return u"]({0}.html)".format(ascii_link(link))
    elif link in subsection_slugs:
        return u"]({0}.html#{1})".format(ascii_link(subsection_slugs[link]), link)
    else:
        print "Unknown:", link
        return link


def ascii_link(link):
    return ascii_filenames.get(link, None) or link


def slugify(title):
    return "".join(c for c in title if c.isalnum() or c in [" ", "-"]).replace(" ", "-").lower()


with open("README.md") as f:
    for line in f:
        if not seen_preamble:
            if line == "---\n":
                seen_preamble = True
                current_section = []
                sections.append((u"简介", "introduction", current_section))
        elif line == "---\n":
            break
        elif line.startswith("## "):
            title = line[3:-1].decode('utf-8')
            if title == u"目录":
                current_section.append(line)
                continue
            current_section = []
            current_section_slug = slugify(title)
            section_slugs.add(current_section_slug)
            sections.append((title, current_section_slug, current_section))
        elif not current_section and line == "\n":
            pass
        elif line.startswith("#"):
            current_section.append(line[1:])
            title = line.replace("#", "")[1:-1].decode('utf-8')
            subsection_slugs[slugify(title)] = current_section_slug
        else:
            current_section.append(line)

ascii_filenames = {
    u'introduction': 'introduction',
    u'hello-world': 'hello-world',
    u'编译与运行': 'compiling-and-running',
    u'声明变量': 'declaring-variables',
    u'原生数据类型及其表示范围': 'primitive-data-types-and-their-limitations',
    u'字符串': 'strings',
    u'条件式': 'conditionals',
    u'集合': 'collections',
    u'循环': 'loops',
    u'函数': 'functions',
    u'类': 'classes',
    u'异常': 'exceptions',
    u'空安全': 'null-safety',
    u'函数式编程': 'functional-programming',
    u'包与导入': 'packages-and-imports',
    u'可见性修饰符': 'visibility-modifiers',
    u'继承': 'inheritance',
    u'对象与伴生对象': 'objects-and-companion-objects',
    u'泛型': 'generics',
    u'扩展函数属性': 'extension-functionsproperties',
    u'成员引用与反射': 'member-references-and-reflection',
    u'注解': 'annotations',
    u'文件-io': 'file-io',
    u'作用域内资源用法': 'scoped-resource-usage',
    u'编写文档': 'documentation',
}


def unicodefy(str_list):
    return [s if isinstance(s, unicode) else s.decode('utf-8') for s in str_list]


def ascii_info(sec_slice):
    info = unicodefy(sec_slice)
    return [info[0], ascii_filenames[info[1]]]


with open("kotlinlang.org.yaml", "w") as yaml:
    for i, (title, slug, section) in enumerate(sections):
        ascii_slug = ascii_filenames[slug]
        filename = "{0:02}-{1}.md".format(i, ascii_slug)
        buf = u"- md: {0}\n  url: {1}.html\n  title: \"{2}\"\n\n".format(filename, ascii_slug, title)
        yaml.write(buf.encode('utf-8'))
        section = unicodefy(section)
        for j, line in enumerate(section):
            section[j] = link_regex.sub(substitute_link, line)
        navigation = []
        if i > 0:
            navigation.append(u"[\u2190 上一节：{0}]({1}.html)".format(*ascii_info(sections[i - 1][0:2])))
        if i < len(sections) - 1:
            navigation.append(u"[下一节：{0} \u2192]({1}.html)".format(*ascii_info(sections[i + 1][0:2])))
        section.append(u"\n\n---\n\n{0}\n".format(" | ".join(navigation)))
        with open(filename, "w") as md:
            if i == 0:
                md.write(copyright_notice.encode('utf-8'))
                md.write(copyright_notice_separator)
            md.write(u"".join(section).encode("utf-8"))
            if i != 0:
                md.write(copyright_notice_separator)
                md.write(copyright_notice.encode('utf-8'))
