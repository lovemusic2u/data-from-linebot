from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from config import get_connection
from flask_paginate import Pagination, get_page_args

showdatapm = Blueprint('showdatapm',__name__)

@showdatapm.route("/")
def Showpm():
    con = get_connection()
    with con.cursor() as cur:
        cur.execute('select count(*) from data_pm')
        total = cur.fetchone()[0]

        page, per_page, offset = get_page_args(page_parameter='page',
                                               per_page_parameter='per_page')

        per_page = 20

        sql = "SELECT * FROM data_pm ORDER BY id DESC LIMIT {} OFFSET {}" \
            .format(per_page, offset)
        cur.execute(sql)
        data = cur.fetchall()

        pagination = Pagination(page=page,
                                per_page=per_page,
                                total=total,
                                css_framework='bootstrap4')

        return render_template('index.html', datas=data, page=page,
                               per_page=per_page,
                               pagination=pagination)

@showdatapm.route("/showsearch",methods=["GET","POST"])
def Showsearch():
    con = get_connection()
    if request.method == "POST":
        if 'ssearch' in request.form:
            searchs = request.form['ssearch']
            with con.cursor() as cur:

                sql = "SELECT * FROM data_pm WHERE location LIKE %s OR location_netka LIKE %s ORDER BY id DESC LIMIT 100"
                cur.execute(sql, ('%' + searchs + '%', '%' + searchs + '%'))
                data = cur.fetchall()

                pagination = ""
                return render_template("index.html", datas=data,pagination=pagination)
        else:
            dcity = request.form['scity']

            with con.cursor() as cur:

                sql = "SELECT * FROM data_pm WHERE county LIKE %s ORDER BY id DESC LIMIT 100"

                cur.execute(sql, ('%'+dcity+'%'))
                data = cur.fetchall()
                pagination = ""
                return render_template("index.html", datas=data,pagination=pagination)

    pagination = ""
    return render_template("index.html",pagination=pagination)
