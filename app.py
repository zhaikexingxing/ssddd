from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import plotly as py
import plotly.graph_objs as go

import csv, re, operator

# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '宋',
    'last_name': '         科',
    'country':'中国',
    'address': '湖北省黄石市黄石港区',
    'birthday':'8月5日',
    'hobby':'电子游戏开发',
    'tel': '1234568910',
    'email': '123321567@qq.com',
    'web': 'https://github.com',
    'web1': '@sk',
    'web2': 'sk',
    'web3': 'sk',
    'introduce': '活泼开朗、乐观向上、兴趣广泛、适应力强、上手快、勤奋好学、脚踏实地、认真负责、坚毅不拔、吃苦耐劳、勇于迎接新挑战。',
    'hobby': '电子游戏开发 ',
    'social_media': [
        {
            'link': 'https://www.facebook.com/nono',
            'icon': 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon': 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon': 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon': 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences': [
        {
            'company': '熊氏有限责任公司',
            'timeframe': '2019.1-2020.5',
            'job': '前端开发经理',
            'description': '1、使佣Div+ css并结合Javascript负责产品的前端开发和页面制作;2、熟悉W3C标准和各主流浏览器在前端开发中的差异，能熟练运用DIV+CSS, 提供针对不同浏览器的前端页面解决方案;3、债相关铲品的需求以及前端程序的实现，提供合理的前端架构;'
        },
        {
            'company': '后端开发公司',
            'timeframe': '2020.1-2021.1',
            'job': '后端开发工程师',
            'description': '1、参与公司大数据项目的整体技术方案设计、技术选型，烷成相应功能模块的代研发与测试; .2、负责公司项目及相关支撑系统的开发及后期维护工作,不断的优化升级,提高户体验。'
        },
        {
            'company': '音乐APP开发公司',
            'timeframe': '2020.1-2021.6',
            'job': '部门开发人员',
            'description': '负责软件的可视化界面和软件的权限设计'
        },
    ],
    'education': [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description': 'Gestion de projets IT, Audit, Programmation',
            'mention': 'Bien',
            'timeframe': '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description': 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention': 'Bien',
            'timeframe': '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description': 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention': 'N/A',
            'timeframe': '2010 - 2012'
        }
    ],
    'programming_languages': {
        'HMTL': ['fa-html5', '100'],
        'CSS': ['fa-css3-alt', '100'],
        'SASS': ['fa-sass', '90'],
        'JS': ['fa-js-square', '90'],
        'Wordpress': ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB': ['fa-database', '60'],
        'MySQL': ['fa-database', '60'],
        'NodeJS': ['fa-node-js', '50']
    },
    'languages': {'French': 'Native', 'English': 'Professional', 'Spanish': 'Professional',
                  'Italian': 'Limited Working Proficiency'},
    'interests': ['Dance', 'Travel', 'Languages']
}


@app.route('/')
def cv(person=person):
    return render_template('source.html', person=person)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))

# 链接一
@app.route('/chart')
def index():
    return render_template('chartsajax.html', graphJSON=gm(),graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON9=gm9())

def gm():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.pie(data,values='total_bill',names='day')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm1():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.histogram(data,x="total_bill",y="tip",color="time",marginal="rug",hover_data=data.columns)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm2():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.bar(data,x="sex",y="tip",color="time",barmode="group")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm3():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.parallel_categories(data,color="size",color_continuous_scale=px.colors.sequential.Inferno)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm4():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.strip(data,x="total_bill",y="time",orientation="h",color="smoker")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm9():
    data = pd.read_csv('tips.csv', encoding='utf-8')
    fig=px.violin(data,y="tip",x="sex",color="smoker",box=True,points="all",hover_data=data.columns)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


# 链接二
@app.route('/chart1')
def index1():
    return render_template('chartsajax1.html',graphJSON5=gm5(),graphJSON6=gm6(),graphJSON7=gm7(),graphJSON8=gm8())

def gm5():
    data = pd.read_csv('Countries Population from 1995 to 2020.csv', encoding='utf-8')
    fig=px.scatter(data,x='Urban Population',y='World Population',color='Country')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm6():
    data = pd.read_csv('Countries Population from 1995 to 2020.csv', encoding='utf-8')
    fig=px.scatter(data,x='Yearly Change',y='Urban Population',color='Country',size="Population",size_max=60)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def gm7():
    data = pd.read_csv('Countries Population from 1995 to 2020.csv', encoding='utf-8')
    fig=px.density_contour(data,x='Yearly Change',y='World Population',color='Country')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def gm8():
    data = pd.read_csv('Countries Population from 1995 to 2020.csv', encoding='utf-8')
    fig=px.density_heatmap(data,x="Median Age",y="Country Global Rank",marginal_x="rug",marginal_y="histogram")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@app.route('/senti')
def main():
    text = ""
    values = {"positive": 0, "negative": 0, "neutral": 0}

    with open('ask_politics.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(reader):
            if idx > 0 and idx % 2000 == 0:
                break
            if 'text' in row:
                nolinkstext = re.sub(
                    r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                    '', row['text'], flags=re.MULTILINE)
                text = nolinkstext

            blob = TextBlob(text)
            for sentence in blob.sentences:
                sentiment_value = sentence.sentiment.polarity
                if sentiment_value >= -0.1 and sentiment_value <= 0.1:
                    values['neutral'] += 1
                elif sentiment_value < 0:
                    values['negative'] += 1
                elif sentiment_value > 0:
                    values['positive'] += 1

    values = sorted(values.items(), key=operator.itemgetter(1))
    top_ten = list(reversed(values))
    if len(top_ten) >= 11:
        top_ten = top_ten[1:11]
    else:
        top_ten = top_ten[0:len(top_ten)]

    top_ten_list_vals = []
    top_ten_list_labels = []
    for language in top_ten:
        top_ten_list_vals.append(language[1])
        top_ten_list_labels.append(language[0])

    graph_values = [{
        'labels': top_ten_list_labels,
        'values': top_ten_list_vals,
        'type': 'pie',
        'insidetextfont': {'color': '#FFFFFF',
                           'size': '14',
                           },
        'textfont': {'color': '#FFFFFF',
                     'size': '14',
                     },
    }]

    layout = {'title': '<b>意见挖掘</b>'}

    return render_template('source.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
