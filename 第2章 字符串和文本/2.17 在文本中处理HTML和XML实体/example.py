import html
s = 'Elements are written as "<tag>text</tag>".'
print(s)  #  Elements are written as "<tag>text</tag>".

print(html.escape(s)) # Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.