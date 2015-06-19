---
layout: post
status: publish
published: true
title: Unit-testing ZF Controllers without Zend_Test
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 198
wordpress_url: http://groovecoder.com/2009/01/08/unit-testing-zf-controllers-without-zend_test/
date: '2009-01-08 13:54:00 -0600'
date_gmt: '2009-01-08 19:54:00 -0600'
categories:
- dev
tags:
- php
- agile
comments:
- id: 132
  author: Duodraco
  author_email: ''
  author_url: ''
  date: '2009-01-09 09:07:00 -0600'
  date_gmt: '2009-01-09 15:07:00 -0600'
  content: Hi Luke. <br/>Great article.<br/>I tagged you in http://duodraco.wordpress.com/2009/01/09/seven-things-that-probably-you-may-not-know-about-me/
    .
- id: 136
  author: rozydesouza
  author_email: ''
  author_url: ''
  date: '2009-08-12 01:09:52 -0500'
  date_gmt: '2009-08-12 07:09:52 -0500'
  content: I have been in search of such interesting Articles, I am on a holiday its
    good to see that everyone are trying their best to keep up the Spirit by having
    such great articles posted.<br /><br />Cheers, Keep it up.<br />___________________<br
    />rozy<br /><a href="http://iwaayinternetmarketing.blogspot.com/" rel="nofollow">We
    do your Marketing for best sales</a>
---
<p>I've read a couple articles and blog posts recently talking about <a href="http://phpimpact.wordpress.com/2008/12/27/phpunit-testing-zend-framework-controllers/">Zend_Test</a> and/or <a href="http://phpimpact.wordpress.com/2008/12/27/phpunit-testing-zend-framework-controllers/">testing Zend Framework Controllers</a>. Particularly for controller testing, I'm kinda surprised how much plumbing code people are using. I recently started testing some Zend_Controller code (from ZF 1.5 even!) at SourceForge and did not do nearly that much plumbing.</p>
<p>Basically, I want to test the controller code in isolation from the front controller, the router, the dispatcher, the views, etc. All I to do is set up a request object, invoke the action methods of the controllers, and then assert against the variables assigned to the view. For these tests, I don't care about the output of the view templates themselves - I just want to know the controllers are putting the right variables into the view object.</p>
<p>It turns out this is actually pretty simple. I made a custom test case:</p>
<div style="width:450px; background-color:#EEEEEE; border:1px solid #CCCCCC; font-family: monospace; font-size: .8em; overflow:auto;">
<pre><br />class Sfx_Controller_TestCase extends Sfx_TestCase<br />{<br />    protected $_request;<br />    protected $_response;<br />    protected $_controller;<br />    <br />    public function setUp()<br />    {<br />        parent::setUp();<br />                <br />        // set up smarty view and restful view helper<br />        $viewRenderer = new Sfx_Controller_Action_Helper_TestViewRenderer();<br />        Zend_Controller_Action_HelperBroker::addHelper($viewRenderer);<br /><br />        $this->_request = new Zend_Controller_Request_Http();<br />        $this->_response = new Zend_Controller_Response_Cli();<br /><br />    }<br />}<br /></pre>
<p></div>
<p>Sfx_TestCase contains all my bootstrap code. However, the only thing I do in bootstrap is set include path and set up a default db adapter for Zend_Db_Table. I don't do anything with Zend_Controller_Front. So this may as well extend straight from PHPUnit_Framework_TestCase. I'm not sure why others are claiming you have to use Zend_Controller_Front to test ZF Controllers - you don't.</p>
<p>I wrote and use Sfx_Controller_Action_Helper_TestViewRenderer (<a href="http://framework.zend.com/wiki/display/ZFPROP/Zend_Test_ViewRenderer">and proposed it as a core class</a>) to simply create an empty Zend_View object into which the controllers can assign variables. Here's the whole class:</p>
<div style="width:450px; background-color:#EEEEEE; border:1px solid #CCCCCC; font-family: monospace; font-size: .8em; overflow:auto;">
<pre><br />class Sfx_Controller_Action_Helper_TestViewRenderer extends Zend_Controller_Action_Helper_ViewRenderer<br />{<br />    public function initView()<br />    {<br />        if (null === $this->view) {<br />            $this->setView(new Zend_View());<br />        }<br />        // Register view with action controller (unless already registered)<br />        if ((null !== $this->_actionController) && (null === $this->_actionController->view)) {<br />            $this->_actionController->view       = $this->view;<br />        }<br />    }<br />}<br /></pre>
<p></div>
<p>With only this much plumbing, I'm able to test the Controllers in isolation - no worrying about routes, dispatchers, plugins, helpers, nor view templates - like so:</p>
<div style="width:450px; background-color:#EEEEEE; border:1px solid #CCCCCC; font-family: monospace; font-size: .8em; overflow:auto;">
<pre><br />class ProjectControllerTest extends Sfx_Controller_TestCase<br />{    <br />    private function __constructProjectController()<br />    {<br />     return new ProjectController($this->_request, $this->_response);<br />    }<br /><br />    public function test_indexAction_fetches_all_projects()<br />    {<br />        $this->_controller = $this->__constructProjectController();<br />        $this->_controller->indexAction(); // assigns 'resources' to view<br />        $this->assertNotNull($this->_controller->view->resources);<br />        $this->assertEquals(27,count($this->_controller->view->resources));<br />    }<br /><br />    public function test_indexAction_new_since_fetches_only_new_projects()<br />    {<br />        $this->_request->setParam('new_since',1205880839);<br />        $this->_controller = $this->__constructProjectController();<br />        $this->_controller->indexAction();<br />        $projects = $this->_controller->view->resources;<br />        $this->assertEquals(4,count($projects));<br />        foreach($projects as $project){<br />            $this->assertGreaterThan(1205880839, $project->create_time);<br />        }<br />    }<br /><br />    public function test_indexAction_limit_limits_projects()<br />    {<br />        $this->_request->setParam('changed_since', 1205880839);<br />        $this->_request->setParam('order_by','changed_since');<br />        $this->_request->setParam('limit', 5);<br />        $this->_controller = $this->__constructProjectController();<br />        $this->_controller->indexAction();<br />        $projects = $this->_controller->view->resources;<br />        $this->assertEquals(5,count($projects));<br />        $prevChangeTime = 0;<br />        foreach($projects as $project){<br />            $this->assertGreaterThanOrEqual($prevRegTime, $project->change_time);<br />            $prevChangeTime = $project->change_time;<br />        }<br />    }<br /><br />}<br /></pre>
<p></div>
<p>I'm finding this to be a much simpler and easier way of testing ZF Controllers than the other articles I've been reading. Now if you <span style="font-weight:bold;">want</span> to test everything in the front controller dispatch process and the view templates, I think Zend_Test is the best bet, but I've not used it yet so I can't be sure. The above classes work fine for what I do.</p>
