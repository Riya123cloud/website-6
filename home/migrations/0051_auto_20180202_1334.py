# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-02 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20180202_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='comrade',
            name='blog_rss_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to the RSS or ATOM feed for your blog.<br>For mentors and coordinators, this is unused. Applicants' blog RSS URLs will be unused. Accepted interns' blog RSS URLs will be used to create an aggregated feed of all Outreachy intern blogs, which will be displayed on the Outreachy website or Outreachy planetaria.", verbose_name='Blog RSS URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='blog_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your blog.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' blog URLs will be shared with their mentors and coordinators. Accepted interns' blog URLs will be displayed on the Outreachy website.", verbose_name='Blog URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='github_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your profile on GitHub.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' GitHub URLs will be shared with their mentors and coordinators. Accepted interns' GitHub URLs will be displayed on the Outreachy website.", verbose_name='GitHub profile URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='gitlab_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your profile on GitLab.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' GitLab URLs will be shared with their mentors and coordinators. Accepted interns' GitLab URLs will be displayed on the Outreachy website.", verbose_name='GitLab profile URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='location',
            field=models.TextField(blank=True, help_text="(Optional) Location - city, state/province, and country.<br>This field is unused for mentors and coordinators. Applicant's location will be shared with their mentors. If selected as an intern, this location will be publicly displayed on the Outreachy website.<br>If you are concerned about keeping your location private, you can share less information, such as just the country, or a larger town nearby.", max_length=100),
        ),
        migrations.AddField(
            model_name='comrade',
            name='nick',
            field=models.TextField(blank=True, help_text="(Optional) The username or 'nick' you typically use when communicating on professional channels. If you don't have one yet, leave this blank and update it later.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' username/nick will be shared with their mentors and coordinators. Accepted interns' username/nick will be displayed on the Outreachy website.", max_length=100, verbose_name='Forum, chat, or IRC username'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='twitter_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your Twitter profile.<br>For mentors and coordinators, this will be displayed to applicants, who may try to contact you via Twitter. Applicants' Twitter URLs will be shared with their mentors and coordinators. Accepted interns' Twitter URLs will be used to create an Outreachy Twitter list for accepted interns for that round. Accepted interns' Twitter URLs will not be displayed on the Outreachy website.", verbose_name='Twitter profile URL'),
        ),
    ]
