from ebike import app

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True, host='localhost', port=8080)

