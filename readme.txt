在执行 python manager.py magrations 时

django 会在相应的 app 的migration文件夹下面生成 一个python脚本文件
在执行 python manager.py migrte 时 django才会生成数据库表，那么django是如何生成数据库表的呢，
django是根据 migration下面的脚本文件来生成数据表的
每个migration文件夹下面有多个脚本，那么django是如何知道该执行那个文件的呢，django有一张django-migrations表，表中记录了已经执行的脚本，那么表中没有的就是还没
执行的脚本，则 执行migrate的时候就只执行表中没有记录的那些脚本。
有时在执行 migrate 的时候如果发现没有生成相应的表，可以看看在 django-migrations表中看看 脚本是否已经执行了，
可以删除 django-migrations 表中的记录 和 数据库中相应的 表 ， 然后重新 执行