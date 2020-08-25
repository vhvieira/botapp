from selenium import webdriver
from classes.Configuration import Configuration
from classes.DriverFactory import DriverFactory
from classes.ConversationClient import ConversationClient
from classes.ConversationFactory import ConversationFactory
import time
import datetime
import html2text

"""
This class defines is a mapping using Selinium Web Driver for the whatsapp web page
"""
class WhatsappWebExecutor:
    def __init__(self):
        print("Loading whatsapp web mapping")
        config = Configuration()
        self.configMessage=config.getConfigValue("configMessage")
        self.configList=config.getConfigValue("configList")
        self.smallInterval=int(config.getConfigValue("shortSleep"))
        self.longInterval=int(config.getConfigValue("longSleep"))
        self.loadSleep=int(config.getConfigValue("loadSleep"))
        self.url=config.getConfigValue("whatsapp_url")
        self.inputClass=config.getConfigValue("inputChatClass")
        self.xPathForChat=config.getConfigValue("xPathForChat")
        self.xPathForSendBtn=config.getConfigValue("xPathForSendBtn")
        self.xPathForLefPane=config.getConfigValue("xPathForLefPane")
        self.xPathForNonRead=config.getConfigValue("xPathForNonRead")
        self.xPathForConversation=config.getConfigValue("xPathForConversation")
        self.xPathForListener=config.getConfigValue("xPathForListener")
        self.xPathForMessages=config.getConfigValue("xPathForMessages")
        self.driverFactory=DriverFactory()
        self.date_formated=datetime.datetime.now().strftime("%d/%m/%Y")
        self.errorMessage=config.getConfigValue("errorMessage")
        self.welcomeEvent=config.getConfigValue("welcomeEvent")
        self.stopContact=config.getConfigValue("stopContact")

    #Method to find the conversation
    def findConversation(self, dest, myNumber):
        driver = self.driverFactory.getDriver(myNumber, self.loadSleep)
        print('Sending message to:' + dest) 
        #[0] is search in the conversation, [1] is chatbox
        chatboxes = driver.find_elements_by_class_name(self.inputClass)
        chatboxes[0].click()
        chatboxes[0].clear()
        chatboxes[0].send_keys(dest)
        time.sleep(self.smallInterval)
        participantList = driver.find_element_by_xpath(self.xPathForLefPane)
        conversation = participantList.find_element_by_xpath(self.xPathForChat.replace("{name}", dest))
        return conversation

    #Method to send message
    def writeMessage(self, conversation, myNumber, message):
        print('writing message message to:' + str(conversation)) 
        driver = self.driverFactory.getDriver(myNumber, self.loadSleep)
        conversation.click()
        time.sleep(self.smallInterval)
        #[0] is search in the conversation, [1] is chatbox
        chatboxes = driver.find_elements_by_class_name(self.inputClass)
        print('Chatbox found:' + str(chatboxes[1])) 
        chatboxes[1].click()
        chatboxes[1].clear()
        chatboxes[1].send_keys(message)
        print('Message sent:' + message) 
        send_icon= driver.find_element_by_xpath(self.xPathForSendBtn)
        send_icon.click()
        time.sleep(self.smallInterval)
        #call go to stop conversation
        self.goToStopContact(myNumber)
    
    def goToStopContact(self, myNumber):
        print('going to stop contact:' + self.stopContact) 
        driver = self.driverFactory.getDriver(myNumber, self.loadSleep)
        leftPane = driver.find_element_by_xpath(self.xPathForLefPane)
        participantList = leftPane.find_element_by_xpath(self.xPathForConversation)
        stopConversation = participantList.find_element_by_xpath(self.xPathForListener.replace("{name}", self.stopContact))
        stopConversation.click()
        time.sleep(self.smallInterval)

    def sendMessage(self, destNumber, message):
        try: 
            client = ConversationClient()  
            conversation = ConversationFactory()          
            print('Text to be sent to dialogflow api is: ' + message)
            if message is None:
                conversation.createNew(destNumber)
                response = client.sendSimpleEvent(self.welcomeEvent)
            else: 
                conversationID = conversation.getConversationID(destNumber)
                response = html2text.html2text(client.sendContinuousMessage(conversationID, message)).strip()
            print( "Dialogflow response: " + str(response))
            return response
        except Exception as ex:
            print('Error sending payload to conversation-api', ex)
            return self.errorMessage

    #TODO: Implement preferences for lang configuration based on myNumber param
    def ReadMessages(self, myNumber, dest):
        print('Starting read messages')
        driver = self.driverFactory.getDriver(myNumber, self.loadSleep)
        leftPane = driver.find_element_by_xpath(self.xPathForLefPane)
        participantList = leftPane.find_element_by_xpath(self.xPathForConversation)
        try:
            print('Reading new messages of pattern:' + dest)
            conversations = participantList.find_elements_by_xpath(self.xPathForListener.replace("{name}", dest))
            for conversation in conversations:
                print('Reading new messsages for ' + conversation.text)
                newConversation = conversation.find_element_by_xpath(self.xPathForNonRead.replace("{name}", dest))
                print('New conversation: ' + str(newConversation))
                if(newConversation is not None):
                    conversation.click()
                    time.sleep(self.smallInterval)
                    conversationDiv = driver.find_element_by_xpath("//div[@id='main']")
                    print('Conversation found, getting texts')
                    texts = conversationDiv.find_elements_by_xpath(self.xPathForMessages.replace("{today}", self.date_formated))
                    if(len(texts) > 0):
                        text = html2text.html2text(texts[-1].text).strip()    
                    #call conversation-api
                    response = self.sendMessage(dest, text)    
                    self.writeMessage(conversation, myNumber, response)
                    #call go to stop conversation
                    self.goToStopContact(myNumber)                 
        except Exception as ex:
            print('Error getting new messages', ex)