
from custom.academy_website.models.models import Teachers
from odoo import http


class AcademyWebsite(http.Controller):

    @http.route('/academy_website/academy_website/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy_website.index', {
            'teachers': Teachers.search([])
        })
        
    @http.route('/academy_website/<name>/', auth='public', website=True)
    def teacherName(self, name):
        return '<h1 style="color:red;">{}Hi ! I am </h1>'.format(name)
    
    @http.route('/academy_website/<int:id>/', auth='public', website=True)
    def teacherId(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
    @http.route('/academy_website/<model("academy.teachers"):student>/', auth='public', website=True)
    def teacher(self, student):
        return http.request.render('academy_website.biography', {
            'person': student
        })

#     @http.route('/academy_website/academy_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_website.listing', {
#             'root': '/academy_website/academy_website',
#             'objects': http.request.env['academy_website.academy_website'].search([]),
#         })

#     @http.route('/academy_website/academy_website/objects/<model("academy_website.academy_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_website.object', {
#             'object': obj
#         })
