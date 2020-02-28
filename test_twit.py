import os
import pytest
from twitter_ import twitter_info

if os.path.exists('./keys'):
	def test_twit1():
		n = twitter_info('keys')
		try:
			n.getting_pics("Friends")
		except():
			assert 0
		else:
			assert 1

	def test_twit2():
		n = twitter_info('keys')
		try:
			n.getting_pics("Penguins")
		except():
			assert 0
		else:
			assert 1

	def test_twit3():
		n = twitter_info('keys')
		try:
			n.getting_pics("Animals")
		except():
			assert 0
		else:
			assert 1

	def test_twit4():
		n = twitter_info('keys')
		try:
			n.getting_pics("Dogs")
		except():
			assert 0
		else:
			assert 1

	def test_twit5():
		n = twitter_info('keys')
		try:
			n.getting_pics("Cats")
		except():
			assert 0
		else:
			assert 1

	def test_twit6():
		n = twitter_info('keys')
		try:
			n.getting_pics("Tigers")
		except():
			assert 0
		else:
			assert 1


else:
	assert 1