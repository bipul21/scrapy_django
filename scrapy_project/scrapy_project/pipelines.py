# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from questions.models import Questions

class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        try:
            question = Questions.objects.get(identifier=item["identifier"])
            print "Question already exist"
            return item
        except Questions.DoesNotExist:
            pass

        question = Questions()
        question.identifier = item["identifier"]
        question.title = item["title"]
        question.url = item["url"]
        question.save()
        return item
