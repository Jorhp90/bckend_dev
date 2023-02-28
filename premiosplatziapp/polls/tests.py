from django.test import TestCase #bateria de tests
from django.urls.base import reverse
from django.utils import timezone

import datetime

from .models import Question

# Create your tests here.
#test models or views
class QuestionModelTests(TestCase): #tests sobre el modelo Question

    def setUp(self):
        self.question = Question(question_text = '¿Quién es el mejor CD de Platzi?')

    def test_was_published_recentyl_with_future_questions(self): #descriptive name
        """ was_published_recently returns False for questions whose pub_date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        self.question.pub_date = time #using setUp method

        self.assertIs( #assert, from intermediate python course
            self.question.was_published_recently(), #attribute was_published_recently -> True
            False #the previous line should be equal to false
            )
        
    def test_was_published_recently_with_present_questions(self):
        """ was_published_recently returns False for questions whose pub_date is in the present """
        time = timezone.now() - datetime.timedelta(hours=2)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), True)

    def test_was_published_recently_with_old_questions(self):
        """ was_published_recently returns False for questions whose pub_date is in the present """
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_published_recently(), False)

class QuestionIndexViewTests(TestCase):
    
    def test_no_questions(self):
        """if no question exist, an appropriate message is displayed"""
        response = self.client.get(reverse('the_polls:index_v')) #make a request to the client and return the url index_v
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    