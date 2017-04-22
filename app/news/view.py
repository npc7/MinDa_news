# ！/usr/bin/python
# -*- coding: utf-8 -*-

from . import news
from .. import db
from flask import jsonify

__author__ = 'AidChow'


@news.route('/list/<page>', methods=['GET'])
def news_list(page):
    page = int(page)
    if page == 0:
        page = 1
    with db.connect().cursor() as cur:
        sql = 'SELECT * from news_list limit %s,%s'
        end = int(page) * 10
        start = (int(page) - 1) * 10
        cur.execute(sql, (start, end - start))
        result = cur.fetchall()
        l = []
        if result is ():
            return jsonify({'code': 200, 'msg': 'load complete', 'content': None})
        for i in result:
            data = {'original_url': i[1], 'content_id': i[2],
                    'news_title': i[3], 'news_push_time': i[4],
                    'news_preview': i[5]}
            l.append(data)
    return jsonify({'code': 200, 'msg': 'request success', 'content': l})


@news.route('/content/<news_id>', methods=['GET'])
def news_content(news_id):
    with db.connect().cursor() as cur:
        sql = 'SELECT * from news_content WHERE news_p_id =%s'
        cur.execute(sql, news_id)
        result = cur.fetchone()
        if result is None:
            return jsonify({'code': 404, 'msg': 'page not found', 'content': None}), 404
        else:
            return jsonify({'code': 200, 'msg': 'request success', 'content': result[2]})
