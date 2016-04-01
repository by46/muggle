import datetime
import httplib

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from polls.models import Poll


# Create your tests here.

class PollMethodTests(TestCase):
    def test_was_published_recently_with_future_poll(self):
        future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertFalse(future_poll.was_published_recently())

    def test_was_published_recently_with_recent_poll(self):
        recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertTrue(recent_poll.was_published_recently())

    def test_was_published_recently_with_old_poll(self):
        old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertFalse(old_poll.was_published_recently())


def create_poll(question, days):
    return Poll.objects.create(question=question,
                               pub_date=timezone.now() + datetime.timedelta(days=days))


class PollViewTests(TestCase):
    def test_index_view_with_no_polls(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, httplib.OK)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_a_past_poll(self):
        create_poll("Past poll", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll>']
        )

    def test_index_view_with_a_future_poll(self):
        create_poll('Future poll', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.', status_code=httplib.OK)
        self.assertQuerysetEqual(
            response.context['latest_poll_list'], []
        )

    def test_index_view_with_future_poll_and_past_poll(self):
        create_poll('Future poll', days=30)
        create_poll('Past poll', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll>']
        )

    def test_index_view_with_two_past_poll(self):
        create_poll('Past poll 1', days=-30)
        create_poll('Past poll 2', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll 2>', '<Poll: Past poll 1>']
        )

    class PollIndexDetailTests(TestCase):
        def test_detail_view_with_a_future_poll(self):
            future_poll = create_poll("Future poll", days=5)
            response = self.client.get(reverse('polls:detail', args=(future_poll.id,)))
            self.assertEqual(response.status_code, httplib.NOT_FOUND)

        def test_detail_view_with_a_past_poll(self):
            past_poll = create_poll('Past poll', days=-5)
            response = self.client.get(reverse('polls:detail', args=(past_poll.id,)))
            self.assertEqual(response.status_code, httplib.OK)
